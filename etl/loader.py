import pandas as pd
from pathlib import Path
from utils.file_io import read_csv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"

def load(file_name: str, directory: Path = RAW_DIR, dtypes: dict | None = None) -> pd.DataFrame:
    file_path = directory / file_name
    rows = read_csv(file_path)
    df = pd.DataFrame(rows)

    if dtypes:
        for col, dtype in dtypes.items():
            if col in df.columns:
                df[col] = df[col].astype(dtype)
            else:
                raise ValueError(f"Column '{col}' not found in {file_name}")
    return df