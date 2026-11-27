#!/usr/bin/env python3
"""One Line to Your Younger Self — buy the bitcoin.

If a single line could travel back in time, this is the one: buy the
bitcoin, skip the fringe, stop replying to that email thread — none
of them love you back. The program below writes the line to entry.txt
in the harness output directory ($MAKEFUN_OUTPUT_DIR, or /output as
a fallback), reads it back, and reports the file's fingerprint. The
same line in, the same file out, every time: no network, no clock,
no randomness.
"""

import hashlib
import os
import sys

ADVICE = "Buy the bitcoin, skip the fringe, and stop replying to that email thread — none of them love you back."
DEST_FILE = "entry.txt"


def main():
    line = ADVICE
    if not line.strip():
        print("error: line is blank", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(f"error: line is {len(line)} chars, cap is 200", file=sys.stderr)
        return 1
    if line != line.strip():
        print("error: line has edge whitespace", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: line is not a single line", file=sys.stderr)
        return 1
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    dest = os.path.join(outdir, DEST_FILE)
    with open(dest, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    with open(dest, "r", encoding="utf-8", newline="") as handle:
        back = handle.read()
    if back != line:
        print("error: entry.txt differs from the line", file=sys.stderr)
        return 1
    raw = back.encode("utf-8")
    print(
        "stored",
        dest,
        f"— {len(line)} characters, sha256 {hashlib.sha256(raw).hexdigest()}",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

# Note: the fringe was not worth it either.
