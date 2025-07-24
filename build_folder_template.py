# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 09:47:51 2025

@author: mik16
"""

from pathlib import Path
import argparse

# Macro-cartelle e relativa descrizione
TOP_LEVEL_FOLDERS = {
    "01_Datasets": """Contiene i dataset usati nel progetto.
- raw/: dataset originali ricevuti o scaricati
- processed/: dataset trasformati o generati""",

    "02_Results": "Risultati degli esperimenti: output, metriche, modelli salvati, ecc.",

    "03_Figures": "Immagini utili alla comunicazione: diagrammi, figure per articoli o presentazioni.",

    "04_Documents": """Documentazione del progetto:
- 01_References/: materiale utile di terzi (slide, articoli, paper)
- 02_Presentations/: presentazioni create da te
- 03_Reports/: report tecnici
- 04_Bureaucracy/: materiale burocratico
- 05_Notes/: appunti interni o note da meeting"""
}

# Sottocartelle da creare (ma senza README)
ALL_SUBFOLDERS = [
    "01_Datasets/raw",
    "01_Datasets/processed",
    "04_Documents/01_References",
    "04_Documents/02_Presentations",
    "04_Documents/03_Reports",
    "04_Documents/04_Bureaucracy",
    "04_Documents/05_Notes"
]

def create_project_structure(project_name: str, destination: Path):
    """
    Crea la struttura base per un progetto, includendo solo README.txt nelle macro-cartelle principali.

    Parametri:
        project_name (str): Nome della cartella principale del progetto.
        destination (Path): Percorso in cui creare la struttura del progetto.
    """
    project_path = destination / project_name
    project_path.mkdir(parents=True, exist_ok=True)

    # Crea tutte le macro-cartelle con README.txt
    for folder, description in TOP_LEVEL_FOLDERS.items():
        folder_path = project_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        readme_file = folder_path / "README.txt"
        readme_file.write_text(description.strip() + "\n", encoding="utf-8")

    # Crea tutte le sottocartelle senza README.txt
    for subfolder in ALL_SUBFOLDERS:
        sub_path = project_path / subfolder
        sub_path.mkdir(parents=True, exist_ok=True)

    print(f"Struttura creata in: {project_path.resolve()}")

def parse_args():
    """
    Analizza gli argomenti da riga di comando.

    Restituisce:
        Namespace con:
            - project_name: nome della cartella progetto
            - destination: percorso in cui creare la struttura
    """
    parser = argparse.ArgumentParser(description="Crea una struttura standard per un nuovo progetto.")
    parser.add_argument("project_name", help="Nome del progetto (usato come nome della cartella principale)")
    parser.add_argument("destination", help="Percorso in cui creare la cartella del progetto")
    return parser.parse_args()


# Per uso interattivo in Spyder, imposta manualmente questi due valori:
project_name = "template_cartella"
destination_path = Path(r"C:\Users\mik16\OneDrive - Università degli Studi di Bari (1)\Projects")

# Esegui la funzione principale
create_project_structure(project_name, destination_path)
