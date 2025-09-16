"""Examples covering custom exceptions and structured error handling."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


class ConfigError(Exception):
    """Raised when the configuration file is missing required data."""


def safe_divide(dividend: float, divisor: float) -> float | None:
    """Divide numbers while handling division-by-zero gracefully."""
    try:
        result = dividend / divisor
    except ZeroDivisionError:
        print("Cannot divide by zero; returning None instead.")
        return None
    else:
        return result
    finally:
        # Demonstrate that finally runs whether or not an exception occurred.
        print("Division attempted.")


def load_config(path: Path) -> Dict[str, Any]:
    """Load JSON config data and validate required fields."""
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ConfigError(f"Invalid JSON configuration: {error}") from error

    if "project" not in data or "author" not in data:
        raise ConfigError("Configuration missing 'project' or 'author'.")

    return data


def main() -> None:
    print("Safe divide 10 / 2 ->", safe_divide(10, 2))
    print("Safe divide 5 / 0 ->", safe_divide(5, 0))

    config_path = Path(__file__).with_name("sample_config.json")
    try:
        data = load_config(config_path)
    except (FileNotFoundError, ConfigError) as error:
        print("Config problem:", error)
    else:
        print("Loaded configuration:", data)


if __name__ == "__main__":
    main()
