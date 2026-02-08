import csv
import json
from typing import Any
from pathlib import Path


def load_from_json(file_path: str | Path) -> Any:
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"file {file_path} does not exist.")
    
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_to_json(file_path: str | Path, data: Any) -> None:
    file_path = Path(file_path)

    if data is None:
        raise ValueError("No data provided to write.")

    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def load_from_csv(file_path: str | Path) -> list[dict[str, str]]:
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File: {file_path} does not exist.")

    with open(file_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        if reader.fieldnames is None:
            raise ValueError("CSV file has no header row.")
        
        rows = list(reader)

    if not rows:
        raise ValueError("CSV file is empty.")

    return rows


def save_to_csv(file_path: str | Path, data: list[dict[str, Any]]) -> None:
    file_path = Path(file_path)
    
    if not data:
        raise ValueError("No data provided to write.")
    
    if not all(isinstance(row, dict) for row in data):
        raise ValueError("All rows must be dictionaries.")

    fieldnames = data[0].keys()

    if not fieldnames:
        raise ValueError("Data has no fields.")
    
    if not all(row.keys() == fieldnames for row in data):
        raise ValueError("Inconsistent fields across rows.")
    
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)