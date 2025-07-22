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
    I metodi sono statici, quindi possono essere usati direttamente dalla classe.
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
