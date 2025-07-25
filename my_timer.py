# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 09:53:02 2025

@author: WKS
"""

import time

class Timer:
    """
    Una classe di utilità che misura e stampa il tempo trascorso durante 
    l'esecuzione di un blocco di codice, utilizzando il costrutto 'with'.

    Esempio d'uso:
        with Timer("Fase di addestramento"):
            train_model()

    Al termine del blocco, stampa il tempo trascorso in formato leggibile.
    """

    def __init__(self, label="Training time"):
        # Etichetta personalizzabile da visualizzare nel log
        self.label = label

    def __enter__(self):
        # Salva il tempo di inizio del blocco
        self.start_time = time.time()
        return self  # opzionale, utile se vuoi accedere a self all'interno del blocco

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Calcola il tempo trascorso alla fine del blocco
        elapsed = time.time() - self.start_time
        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        seconds = elapsed % 60

        # Stampa il tempo trascorso in un formato leggibile
        if hours > 0:
            print(f"{self.label}: {hours} h, {minutes} min e {seconds:.2f} sec")
        elif minutes > 0:
            print(f"{self.label}: {minutes} min e {seconds:.2f} sec")
        else:
            print(f"{self.label}: {seconds:.2f} sec")
