#!/usr/bin/env python3
"""Print the houseplant out-of-office line from entry.txt."""

from pathlib import Path


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    # Strip only the trailing newline so the printed line is exact.
    line = entry_path.read_text(encoding="utf-8").rstrip("\n")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
