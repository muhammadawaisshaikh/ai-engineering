"""
Root package initializer.
Exposes:
- load_dataset: Load CSV into a pandas DataFrame.
- preprocess_data: Clean and prepare the DataFrame.
"""

from .data_loader import load_dataset
from .preprocessing import preprocess_data

__all__ = ["load_dataset", "preprocess_data"]