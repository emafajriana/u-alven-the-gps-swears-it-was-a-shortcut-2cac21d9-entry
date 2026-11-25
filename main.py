#!/usr/bin/env python3
"""GPS excuse entry for make.fun: The GPS Swears It Was a Shortcut.

Writes the GPS's one-line excuse to /output/entry.txt. The entry is a
single plain-text line, at most 200 characters, in the GPS's own smug,
defensive voice, blaming the map for the wrong road.
"""

import os
import sys

ENTRY = (
    "That cul-de-sac has a lovely view of the wedding "
    "you are now late for. The map's fault, obviously."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """Enforce the competition gate: 1-200 UTF-8 chars, one line, not blank."""
    if not text or not text.strip():
        raise ValueError("entry is empty")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if len(text.splitlines()) != 1:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")
    # Read back byte-exact: what the judge sees must be what we wrote.
    with open(path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != ENTRY + "\n":
        raise ValueError("entry.txt read-back mismatch")
    print(f"entry.txt written: {len(ENTRY)} chars", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
