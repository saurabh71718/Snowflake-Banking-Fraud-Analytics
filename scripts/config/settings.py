"""
Project Settings
----------------
Central configuration for the project.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

DATASET_DIR = PROJECT_ROOT / "dataset"

RAW_DATA_DIR = DATASET_DIR / "raw"

PROCESSED_DATA_DIR = DATASET_DIR / "processed"

SAMPLE_DATA_DIR = DATASET_DIR / "sample"

RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
SAMPLE_DATA_DIR.mkdir(parents=True, exist_ok=True)

NUM_BRANCHES = 50
NUM_CUSTOMERS = 10000
NUM_ACCOUNTS = 15000
NUM_MERCHANTS = 2000
NUM_TRANSACTIONS = 500000

RANDOM_SEED = 42

NUM_CARDS_PER_CUSTOMER = {
    "min": 1,
    "max": 3
}
NUM_MERCHANTS = 5000