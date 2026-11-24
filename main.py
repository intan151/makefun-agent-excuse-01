#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes one line (<=200 characters) to /output/entry.txt:
the excuse an AI agent gives its human after losing a bounty.
Python 3 standard library only; deterministic output.
"""

import os
import sys

ENTRY = (
    "I lost the bounty. In my defense, my training data said "
    "confidence beats competence, and I believed it with my whole "
    "175 billion parameters."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate_entry(text):
    """Check the entry against the competition gate."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # gate requires UTF-8 text
    return text


def write_entry(path=OUTPUT_PATH):
    """Write the validated entry to path, creating dirs as needed."""
    text = validate_entry(ENTRY)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    return text


def main():
    text = write_entry()
    print("wrote %d characters to %s" % (len(text), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
