# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 09:47:23 2025

@author: WKS
"""

import sys
from pathlib import Path
import getpass

class ProjectPaths:
    """
    Classe per gestire la struttura di directory di un progetto locale sincronizzato via OneDrive.

    Attributi:
    ----------
    project : str
        Nome del progetto (sottocartella in 'Projects').
    base_path : Path
        Percorso base del progetto.
    datasets_root : Path
        Directory 01_Datasets.
    results_root : Path
        Directory 02_Results.
    figures_root : Path
        Directory 03_Figures.
    documents_root : Path
        Directory 04_Documents.
    user : str
        Nome utente corrente.
    
    Metodi:
    -------
    get_datasets_path(*path_parts, processed=False)
        Restituisce un path dentro 01_Datasets (processed=True per sottocartella 'processed').

    get_results_path(*path_parts, plots=False)
        Restituisce un path dentro 02_Results, opzionalmente con sottocartella 'plots/'.

    get_figures_path(*path_parts, plots=False)
        Restituisce un path dentro 03_Figures, opzionalmente con sottocartella 'plots/'.
    """

    def __init__(self, project, append_subdirs=None):
        self.project = project
        self.user = getpass.getuser()
        self.base_path = self._set_project_directory()

        # Inizializzazione root delle macro-cartelle
        self.datasets_root = self.base_path / "01_Datasets"
        self.results_root = self.base_path / "02_Results"
        self.figures_root = self.base_path / "03_Figures"

        self._append_to_syspath(append_subdirs)

    def _set_project_directory(self):
        one_drive_paths = [
            Path(fr"C:\Users\{self.user}\OneDrive - Università degli Studi di Bari (1)\Projects"),
            Path(fr"C:\Users\{self.user}\OneDrive - Università degli Studi di Bari\Projects")
        ]
        for base in one_drive_paths:
            project_path = base / self.project
            if project_path.exists():
                # Imposta la working directory
                print(f"Directory di lavoro impostata su: {project_path}")
                return project_path

        raise FileNotFoundError(
            f"Nessuna directory trovata per il progetto '{self.project}' nelle cartelle OneDrive dell’utente '{self.user}'."
        )

    def _append_to_syspath(self, subdirs):
        if not subdirs:
            return

        github_root = Path(fr"C:\Users\{self.user}\Github")
        if not github_root.exists():
            raise ValueError(f"Directory 'Github' non trovata per l’utente '{self.user}'.")

        for sub in subdirs:
            full_path = github_root / sub
            if full_path.exists():
                sys.path.append(str(full_path))
                print(f"Aggiunto a sys.path: {full_path}")
            else:
                print(f"Attenzione: sottocartella '{sub}' non trovata in {github_root}")

    def get_datasets_path(self, *path_parts, processed=False):
        """
        Restituisce uno o due path nella cartella 01_Datasets.
    
        Parametri:
        - path_parts: sottopercorsi (es. "input", "gennaio")
        - processed:
            - False: restituisce solo 01_Datasets/raw/...
            - True: restituisce solo 01_Datasets/processed/...
            - "both": restituisce entrambi (raw_path, processed_path)
    
        Ritorna:
        - Path oppure Tuple[Path, Path]
        """
        raw_path = self.datasets_root / "raw" / Path(*path_parts)
        proc_path = self.datasets_root / "processed" / Path(*path_parts)
    
        if processed == "both":
            raw_path.mkdir(parents=True, exist_ok=True)
            proc_path.mkdir(parents=True, exist_ok=True)
            print(f"Cartella dataset raw: {raw_path}")
            print(f"Cartella dataset processed: {proc_path}")
            return raw_path, proc_path
    
        selected = proc_path if processed else raw_path
        selected.mkdir(parents=True, exist_ok=True)
        label = "processed" if processed else "raw"
        print(f"Cartella dataset ({label}): {selected}")
        return selected

    def get_results_path(self, *path_parts, plots=False):
        """
        Restituisce uno o due path all'interno della cartella 02_Results.

        Parametri
        ----------
        path_parts : str
            Componenti del path (es. regione, orientamento, peso).
            Esempio: region, "Direct", "Weighted"

        plots : bool, default=False
            Se True, crea anche una sottocartella 'plots/' e la restituisce.

        Returns
        -------
        tuple(Path, Path or None)
            - Primo elemento: Path completo dei risultati.
              Es: 02_Results/<region>/<direction>/<weight>/
            - Secondo elemento: Path della cartella plots oppure None.
              Es: 02_Results/<region>/<direction>/<weight>/plots/
        """
        # Costruisce il path dei risultati
        base_path = self.results_root.joinpath(*path_parts)
        base_path.mkdir(parents=True, exist_ok=True)

        plots_path = None

        if plots:
            # Se richiesto, crea anche la sottocartella plots
            plots_path = base_path / "plots"
            plots_path.mkdir(parents=True, exist_ok=True)

        # Stampa diagnostica
        print(f"[ProjectPaths] Cartella risultati: {base_path}")
        if plots_path:
            print(f"[ProjectPaths] Cartella plots: {plots_path}")

        return base_path, plots_path

    def get_figures_path(self, *path_parts):
        """
        Restituisce un path nella cartella 03_Figures, opzionalmente con 'plots/' in coda.
        """
        path = self.figures_root.joinpath(*path_parts)
        path.mkdir(parents=True, exist_ok=True)
        print(f"Cartella figure: {path}")
        return path