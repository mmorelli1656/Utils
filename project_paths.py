# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 09:47:23 2025

@author: WKS
"""

import sys
import getpass
from pathlib import Path
from typing import Optional, Tuple, Union


class ProjectPaths:
    """
    Class to manage the directory structure of a local project synced via OneDrive.

    Attributes
    ----------
    project : str
        Project name (subfolder in 'Projects').
    base_path : Path
        Base path of the selected project.
    datasets_root : Path
        Path to '01_Datasets' folder.
    results_root : Path
        Path to '02_Results' folder.
    figures_root : Path
        Path to '03_Figures' folder.
    user : str
        Current system username.

    Methods
    -------
    get_datasets_path(*path_parts, processed=False)
        Returns a path inside '01_Datasets', optionally inside 'processed/'.
    
    get_results_path(*path_parts, plots=False)
        Returns a path inside '02_Results', optionally with a 'plots/' subfolder.

    get_figures_path(*path_parts)
        Returns a path inside '03_Figures'.
    """

    def __init__(self, project: str, append_subdirs: Optional[list] = None):
        self.project = project
        self.user = getpass.getuser()
        self.base_path = self._find_onedrive_project_path()

        # Initialize root folders
        self.datasets_root = self.base_path / "01_Datasets"
        self.results_root = self.base_path / "02_Results"
        self.figures_root = self.base_path / "03_Figures"

        # Optionally append subdirectories to sys.path
        self._append_to_syspath(append_subdirs)

    def _find_onedrive_project_path(self) -> Path:
        """
        Attempts to locate the project folder in common OneDrive locations.

        Returns
        -------
        Path
            Path to the project directory if found.

        Raises
        ------
        FileNotFoundError
            If the project directory is not found.
        """
        candidate_paths = [
            Path(fr"C:\Users\{self.user}\OneDrive - Università degli Studi di Bari (1)\Projects"),
            Path(fr"C:\Users\{self.user}\OneDrive - Università degli Studi di Bari\Projects")
        ]
        for base in candidate_paths:
            project_path = base / self.project
            if project_path.exists():
                print(f"[INFO] Working directory set to: {project_path}")
                return project_path

        raise FileNotFoundError(
            f"[ERROR] Project '{self.project}' not found in OneDrive folders for user '{self.user}'."
        )

    def _append_to_syspath(self, subdirs: Optional[list]):
        """
        Appends given subdirectories (within GitHub folder) to sys.path.

        Parameters
        ----------
        subdirs : list of str
            List of subdirectory names to append.
        """
        if not subdirs:
            return

        github_root = Path(fr"C:\Users\{self.user}\Github")
        if not github_root.exists():
            raise ValueError(f"[ERROR] 'Github' directory not found for user '{self.user}'.")

        for sub in subdirs:
            full_path = github_root / sub
            if full_path.exists():
                sys.path.append(str(full_path))
                print(f"[INFO] Added to sys.path: {full_path}")
            else:
                print(f"[WARNING] Subdirectory not found: {full_path}")

    def _get_subfolder_path(
        self,
        root: Path,
        *path_parts: str,
        subfolder: Optional[str] = None,
        create: bool = True
    ) -> Path:
        """
        Builds and optionally creates a nested path inside a given root.

        Parameters
        ----------
        root : Path
            Root directory.
        path_parts : str
            Subfolder names.
        subfolder : str, optional
            Additional subfolder to append at the end.
        create : bool
            Whether to create the path if it does not exist.

        Returns
        -------
        Path
            Full path constructed.
        """
        path = root.joinpath(*path_parts)
        if subfolder:
            path = path / subfolder
        if create:
            path.mkdir(parents=True, exist_ok=True)
        return path

    def get_datasets_path(
        self, *path_parts: str, processed: Union[bool, str] = False
    ) -> Union[Path, Tuple[Path, Path]]:
        """
        Returns one or both paths inside '01_Datasets'.

        Parameters
        ----------
        path_parts : str
            Subfolder components, e.g., "input", "2023".
        processed : bool or 'both'
            - False: returns raw path only
            - True: returns processed path only
            - 'both': returns (raw_path, processed_path)

        Returns
        -------
        Path or Tuple[Path, Path]
            Requested path(s).
        """
        raw_path = self._get_subfolder_path(self.datasets_root, "raw", *path_parts)
        proc_path = self._get_subfolder_path(self.datasets_root, "processed", *path_parts)

        if processed == "both":
            print(f"[INFO] Dataset folder (raw): {raw_path}")
            print(f"[INFO] Dataset folder (processed): {proc_path}")
            return raw_path, proc_path

        selected = proc_path if processed else raw_path
        label = "processed" if processed else "raw"
        print(f"[INFO] Dataset folder ({label}): {selected}")
        return selected

    def get_results_path(
        self, *path_parts: str, plots: bool = False
    ) -> Tuple[Path, Optional[Path]]:
        """
        Returns a path inside '02_Results', optionally with a 'plots' subfolder.

        Parameters
        ----------
        path_parts : str
            Components like region, model name, etc.
        plots : bool
            If True, creates and returns a 'plots/' subfolder as well.

        Returns
        -------
        Tuple[Path, Optional[Path]]
            - Main result path
            - Plots path (if plots=True), otherwise None
        """
        base_path = self._get_subfolder_path(self.results_root, *path_parts)
        plots_path = None

        if plots:
            plots_path = self._get_subfolder_path(base_path, subfolder="plots")

        print(f"[INFO] Results folder: {base_path}")
        if plots_path:
            print(f"[INFO] Plots folder: {plots_path}")

        return base_path, plots_path

    def get_figures_path(self, *path_parts: str) -> Path:
        """
        Returns a path inside '03_Figures'.

        Parameters
        ----------
        path_parts : str
            Subfolder components.

        Returns
        -------
        Path
            Full path.
        """
        path = self._get_subfolder_path(self.figures_root, *path_parts)
        print(f"[INFO] Figures folder: {path}")
        return path
