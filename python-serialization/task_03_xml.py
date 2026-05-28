"""Serialize and deserialize dictionaries to/from XML files."""
from __future__ import annotations

import xml.etree.ElementTree as ET
from typing import Dict


def serialize_to_xml(dictionary: Dict[str, str], filename: str) -> None:
    root = ET.Element("root")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename: str) -> Dict[str, str]:
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result: Dict[str, str] = {}
        for child in root:
            result[child.tag] = child.text if child.text is not None else ""
        return result
    except Exception:
        return {}
