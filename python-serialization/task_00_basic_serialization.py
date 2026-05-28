'''Basic serialization helpers for Holberton project.'''
from __future__ import annotations

import json
from typing import Any, Dict


def serialize_and_save_to_file(data: Dict[str, Any], filename: str) -> None:
    '''Serialize a Python dictionary to a JSON file.'''
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename: str) -> Dict[str, Any]:
    """Load JSON from a file and deserialize it into a python dict"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
