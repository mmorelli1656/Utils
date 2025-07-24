# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 09:47:23 2025

@author: WKS
"""

import sys
# import os
from pathlib import Path
import getpass

# class ProjectPaths:
#     """
#     Classe di utilità per gestire i percorsi relativi a un progetto locale.

#     Questa classe imposta automaticamente la directory di lavoro in base al nome del progetto 
#     e alla struttura delle cartelle presenti su OneDrive, e fornisce metodi comodi per accedere 
#     a directory comuni come quelle di immagini e risultati.

#     Opzionalmente, può anche aggiungere percorsi relativi a moduli locali (es. da una cartella Github) 
#     al `sys.path` per facilitarne l'importazione.

#     Attributi:
#     ----------
#     project : str
#         Nome del progetto (corrispondente a una sottocartella in OneDrive/Projects).
#     base_path : Path
#         Percorso base del progetto (impostato automaticamente).
#     image_root : Path
#         Percorso alla directory delle immagini (`03_Images` dentro il progetto).
#     results_root : Path
#         Percorso alla directory dei risultati (`04_Results` dentro il progetto).
#     user : str
#         Nome utente Windows corrente (ottenuto con getpass.getuser()).

#     Metodi:
#     -------
#     get_image_path(*path_parts)
#         Ritorna e crea (se non esiste) un percorso nella cartella immagini.
    
#     get_results_path(*path_parts)
#         Ritorna e crea (se non esiste) un percorso nella cartella dei risultati.
    
#     get_save_paths(*path_parts)
#         Ritorna una tupla con i percorsi completi per immagini e risultati.
#     """

#     def __init__(self, project, append_subdirs=None):
#         self.project = project
#         self.user = getpass.getuser()
#         self.base_path = self._set_project_directory()
#         self.image_root = self.base_path / "03_Images"
#         self.results_root = self.base_path / "04_Results"
#         self._append_to_syspath(append_subdirs)

#     def _set_project_directory(self):
#         one_drive_paths = [
#             Path(fr"C:\Users\{self.user}\OneDrive - Università degli Studi di Bari (1)\Projects"),
#             Path(fr"C:\Users\{self.user}\OneDrive - Università degli Studi di Bari\Projects")
#         ]
#         for base in one_drive_paths:
#             project_path = base / self.project
#             if project_path.exists():
#                 os.chdir(project_path)
#                 print(f"Directory di lavoro impostata su: {project_path}")
#                 return project_path

#         raise FileNotFoundError(
#             f"Nessuna directory valida trovata per il progetto '{self.project}' in OneDrive per l’utente '{self.user}'."
#         )

#     def _append_to_syspath(self, subdirs):
#         if not subdirs:
#             return

#         github_root = Path(fr"C:\Users\{self.user}\Github")
#         if not github_root.exists():
#             raise ValueError(f"Directory 'Github' non trovata per l’utente '{self.user}'.")

#         for sub in subdirs:
#             full_path = github_root / sub
#             if full_path.exists():
#                 sys.path.append(str(full_path))
#                 print(f"Aggiunto al sys.path: {full_path}")
#             else:
#                 print(f"Attenzione: sottocartella '{sub}' non trovata in {github_root}")

#     def get_image_path(self, *path_parts):
#         path = self.image_root.joinpath(*path_parts)
#         path.mkdir(parents=True, exist_ok=True)
#         print(f"Cartella immagini: {path}")
#         return path

#     def get_results_path(self, *path_parts):
#         path = self.results_root.joinpath(*path_parts)
#         path.mkdir(parents=True, exist_ok=True)
#         print(f"Cartella risultati: {path}")
#         return path

#     def get_save_paths(self, *path_parts):
#         return self.get_image_path(*path_parts), self.get_results_path(*path_parts)
    

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
        Restituisce un path nella cartella 01_Datasets, opzionalmente in 'processed/'.
        """
        root = self.datasets_root / ("processed" if processed else "raw")
        path = root.joinpath(*path_parts)
        path.mkdir(parents=True, exist_ok=True)
        print(f"Cartella dataset ({'processed' if processed else 'raw'}): {path}")
        return path

    def get_results_path(self, *path_parts, plots=False):
        """
        Restituisce uno o due path nella cartella 02_Results.
    
        Se plots=False:
            → restituisce il path: 02_Results/<path_parts>/
    
        Se plots=True:
            → restituisce una tupla:
               (02_Results/<path_parts>/, 02_Results/<path_parts>/plots/)
        """
        base_path = self.results_root.joinpath(*path_parts)
        base_path.mkdir(parents=True, exist_ok=True)
    
        if plots:
            plots_path = base_path / "plots"
            plots_path.mkdir(parents=True, exist_ok=True)
            print(f"Cartella risultati: {base_path}")
            print(f"Cartella plots: {plots_path}")
            return base_path, plots_path
    
        print(f"Cartella risultati: {base_path}")
        return base_path

    def get_figures_path(self, *path_parts):
        """
        Restituisce un path nella cartella 03_Figures, opzionalmente con 'plots/' in coda.
        """
        path = self.figures_root.joinpath(*path_parts)
        path.mkdir(parents=True, exist_ok=True)
        print(f"Cartella figure: {path}")
        return path