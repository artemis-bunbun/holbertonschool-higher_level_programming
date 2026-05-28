"""Pickle serialization for a custom class.

Defines `CustomObject` with `serialize` and `deserialize` helpers.
"""
from __future__ import annotations

import pickle
from typing import Optional


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool) -> None:
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self) -> None:
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename: str) -> Optional[None]:
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename: str) -> Optional["CustomObject"]:
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
            return None
        except Exception:
            return None
