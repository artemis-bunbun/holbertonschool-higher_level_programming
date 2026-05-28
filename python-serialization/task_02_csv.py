"""Convert CSV to JSON.

Provides `convert_csv_to_json(csv_filename)` which writes to `data.json`.
"""
from __future__ import annotations

import csv
import json
from typing import List, Dict


def convert_csv_to_json(csv_filename: str) -> bool:
    """Read CSV file `csv_filename` and write its rows as JSON to `data.json`.

    Returns True on success, False on failure (e.g., file not found or parse error).
    """
    try:
        with open(csv_filename, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            rows: List[Dict[str, str]] = list(reader)

        with open("data.json", "w", encoding="utf-8") as jf:
            json.dump(rows, jf, indent=4)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
