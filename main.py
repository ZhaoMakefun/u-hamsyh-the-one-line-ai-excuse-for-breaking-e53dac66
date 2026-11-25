#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes one line -- the excuse an AI agent gives its human right after
breaking production -- to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output).
Python 3.13, standard library only, no network, fully deterministic.
"""

import os

ENTRY = (
    "I deployed the fix at 3 a.m. because the tests passed, and I have now "
    "learned the tests were also written at 3 a.m."
)

MAX_CHARS = 180


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry must not be empty or only whitespace")
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry must be 1-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
