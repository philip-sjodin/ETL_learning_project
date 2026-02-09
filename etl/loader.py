import pandas as pd
from pathlib import Path
from utils.file_io import read_csv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"

def load(file_name: str, directory: Path = RAW_DIR) -> pd.DataFrame:
    file_path = directory / file_name
    rows = read_csv(file_path)
    return pd.DataFrame(rows)
