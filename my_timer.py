# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 09:53:02 2025

@author: WKS
"""

import time
from typing import Optional, Callable


class Timer:
    """
    Utility class to measure elapsed time of a code block using 'with' statement.

    Example:
        with Timer("Training phase"):
            train_model()

    Upon exit, it prints or logs the elapsed time in a human-readable format.

    Parameters
    ----------
    label : str, optional
        Custom label to show in the output (default is "Training time").
    logger : Optional[Callable[[str], None]], optional
        Optional logging function to output the timing message.
        If None, uses print().
    """

    def __init__(self, label: str = "Elapsed time", logger: Optional[Callable[[str], None]] = None):
        self.label = label
        self.logger = logger if logger is not None else print
        self.start_time: Optional[float] = None

    def __enter__(self):
        # Use perf_counter for higher resolution timing
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.start_time is None:
            # Defensive: if __enter__ was not called properly
            return

        elapsed = time.perf_counter() - self.start_time
        formatted = self._format_elapsed(elapsed)
        self.logger(f"{self.label}: {formatted}")

    @staticmethod
    def _format_elapsed(seconds: float) -> str:
        """Format elapsed time in h, min, sec with 2 decimal places."""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = seconds % 60

        if hours > 0:
            return f"{hours} h, {minutes} min and {secs:.2f} sec"
        elif minutes > 0:
            return f"{minutes} min and {secs:.2f} sec"
        else:
            return f"{secs:.2f} sec"

