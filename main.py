"""Запускає демонстрації патернів у порядку нумерації."""

from pathlib import Path
from runpy import run_path


CATEGORIES = ("creational", "structural", "behavioral")


def main() -> None:
    """Знаходить і запускає приклади відносно кореня репозиторію."""
    root = Path(__file__).resolve().parent
    for category in CATEGORIES:
        examples = (root / category).glob("[0-9][0-9]_*/example.py")
        for example in sorted(examples):
            print(f"\n=== {example.parent.name} ===")
            run_path(str(example), run_name="__main__")


if __name__ == "__main__":
    main()
