# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 09:54:54 2025

@author: WKS
"""

import pickle
from pathlib import Path

class PickleHandler:
    """
    Classe utility per salvare e caricare oggetti Python utilizzando pickle.
    I metodi mantengono nomi familiari: `save_pickle` e `load_pickle`.
    """

    def __init__(self, verbose=True):
        self.verbose = verbose

    def save_pickle(self, obj, file_path):
        """
        Salva un oggetto Python su file usando pickle.

        Parameters
        ----------
        obj : qualsiasi
            L'oggetto da salvare.
        file_path : str o Path
            Il percorso del file.
        """
        file_path = Path(file_path)
        with open(file_path, 'wb') as f:
            pickle.dump(obj, f)
        if self.verbose:
            print(f"[PickleHandler] Oggetto salvato in: {file_path}")

    def load_pickle(self, file_path):
        """
        Carica un oggetto Python da un file pickle.

        Parameters
        ----------
        file_path : str o Path
            Il percorso del file pickle.

        Returns
        -------
        obj : qualsiasi
            L'oggetto caricato.
        """
        file_path = Path(file_path)
        with open(file_path, 'rb') as f:
            obj = pickle.load(f)
        if self.verbose:
            print(f"[PickleHandler] Oggetto caricato da: {file_path}")
        return obj
