"""One Line, One Laugh -- make.fun entry.

Reads the single joke line from entry.txt (shipped beside this file),
validates it against the bounty gate (1-140 characters, not only
whitespace), writes it to /output/entry.txt for the judge, and prints it.
"""

from pathlib import Path

MAX_CHARS = 140
OUTPUT_PATH = Path("/output/entry.txt")


def write_output(line: str) -> None:
    """Write the validated line where the sealed scorer reads it."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")


def load_line() -> str:
    path = Path(__file__).with_name("entry.txt")
    return path.read_text(encoding="utf-8").strip()


def validate(line: str) -> str:
    """Enforce the gate: one non-empty line, 1-140 characters."""
    if not line or len(line) > MAX_CHARS:
        raise SystemExit("entry line must be 1-140 characters")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    return line


def main() -> None:
    line = validate(load_line())
    write_output(line)
    print(line)


if __name__ == "__main__":
    main()
