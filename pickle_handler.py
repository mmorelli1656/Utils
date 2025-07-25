# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 09:54:54 2025

@author: WKS
"""

import pickle
from pathlib import Path
import networkx as nx

class PickleHandler:
    """
    Classe utility per salvare e caricare oggetti Python, inclusi grafi, usando pickle.

    Metodi statici per:
    - Salvataggio/caricamento generico di oggetti (`.pkl`)
    - Salvataggio/caricamento di grafi con estensione `.gpickle` (solo convenzione)
    """

    @staticmethod
    def save_pickle(obj, file_path):
        """
        Salva un oggetto Python su file usando pickle.
        """
        file_path = Path(file_path)
        with open(file_path, 'wb') as f:
            pickle.dump(obj, f)
        print(f"[PickleHandler] Oggetto salvato in: {file_path}")

    @staticmethod
    def load_pickle(file_path):
        """
        Carica un oggetto Python da un file pickle.
        """
        file_path = Path(file_path)
        with open(file_path, 'rb') as f:
            obj = pickle.load(f)
        print(f"[PickleHandler] Oggetto caricato da: {file_path}")
        return obj

    @staticmethod
    def save_graph(graph, file_path):
        """
        Salva un grafo NetworkX in formato .gpickle.
        """
        file_path = Path(file_path)
        nx.write_gpickle(graph, file_path)
        print(f"[PickleHandler] Grafo salvato in: {file_path}")

    @staticmethod
    def load_graph(file_path):
        """
        Carica un grafo NetworkX da un file .gpickle.
        """
        file_path = Path(file_path)
        graph = nx.read_gpickle(file_path)
        print(f"[PickleHandler] Grafo caricato da: {file_path}")
        return graph
