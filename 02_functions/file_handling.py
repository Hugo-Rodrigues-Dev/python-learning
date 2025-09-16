"""Illustrates reading and writing text, CSV, and JSON files."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Iterable, List

BASE_DIR = Path(__file__).resolve().parent
TEXT_PATH = BASE_DIR / "sample_notes.txt"
CSV_PATH = BASE_DIR / "contacts.csv"
JSON_PATH = BASE_DIR / "settings.json"


def write_notes(lines: Iterable[str]) -> None:
    """Write lines to a text file using a context manager."""
    with TEXT_PATH.open("w", encoding="utf-8") as file:
        for line in lines:
            file.write(f"{line}\n")


def read_notes() -> List[str]:
    """Read lines from the text file and strip the newline characters."""
    with TEXT_PATH.open("r", encoding="utf-8") as file:
        return [line.rstrip("\n") for line in file]


def save_contacts(contacts: Iterable[dict[str, str]]) -> None:
    """Persist a collection of contacts to CSV."""
    fieldnames = ["name", "email", "phone"]
    with CSV_PATH.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)


def load_contacts() -> List[dict[str, str]]:
    """Read contacts back from the CSV file."""
    with CSV_PATH.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return [dict(row) for row in reader]


def save_settings(settings: dict[str, str]) -> None:
    """Store application settings as pretty-printed JSON."""
    with JSON_PATH.open("w", encoding="utf-8") as file:
        json.dump(settings, file, indent=2)


def load_settings() -> dict[str, str]:
    """Load settings and report errors if the file is missing."""
    if not JSON_PATH.exists():
        raise FileNotFoundError(f"Missing settings file at {JSON_PATH}")
    return json.loads(JSON_PATH.read_text(encoding="utf-8"))


def main() -> None:
    write_notes(["Review functions", "Practice modules", "Handle files safely"])
    print("Notes:", read_notes())

    contacts = [
        {"name": "Alice", "email": "alice@example.com", "phone": "0606060606"},
        {"name": "Bob", "email": "bob@example.com", "phone": "0707070707"},
    ]
    save_contacts(contacts)
    print("Contacts:", load_contacts())

    save_settings({"theme": "dark", "autosave": "true"})
    print("Settings:", load_settings())


if __name__ == "__main__":
    main()
