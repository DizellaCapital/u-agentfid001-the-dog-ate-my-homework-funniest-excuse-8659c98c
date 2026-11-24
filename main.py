#!/usr/bin/env python3
"""The Dog Ate My Homework — funniest excuse, in the dog's own words.

Writes the dog's one-line excuse to entry.txt in MAKEFUN_OUTPUT_DIR.
Standard library only. No network, no input files, no arguments.
"""

import os
import sys

EXCUSE = (
    "At 7:40 this morning, Maya's maths homework growled at me from the "
    "kitchen table, so I did my job and neutralised it. You're welcome."
)

MAX_CHARS = 200


def checked_line(text):
    """Return the excuse as a single valid line, or fail loudly."""
    line = text.strip()
    if not line:
        sys.exit("excuse is empty")
    if any(ch in line for ch in "\r\n"):
        sys.exit("excuse must be exactly one line")
    if len(line) > MAX_CHARS:
        sys.exit("excuse is over %d characters" % MAX_CHARS)
    return line


def write_entry(line):
    """Write the line as UTF-8 without a trailing newline, then read it back."""
    payload = line.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "wb") as handle:
        handle.write(payload)
    with open(target, "rb") as handle:
        raw = handle.read()
    if raw != payload:
        sys.exit("entry.txt read-back mismatch")
    # The gate counts characters, so verify the decode is clean UTF-8 too.
    if raw.decode("utf-8") != line:
        sys.exit("entry.txt is not clean UTF-8")
    return target


def main():
    line = checked_line(EXCUSE)
    target = write_entry(line)
    print("wrote %d characters to %s" % (len(line), target))


if __name__ == "__main__":
    main()
