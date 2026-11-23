#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the funniest single-line safety warning label that should come
printed on every human being to /output/entry.txt.

The label is one line, 160 characters or fewer, funny first and plausible
second: it reads like a real printed warning label, it is true about how
people actually behave, and the laugh lands in the last few words.
"""

import os

LABEL = (
    "WARNING: This human reads the instructions, "
    "ignores them completely, then blames the instructions."
)

MAX_CHARS = 160


def main() -> None:
    label = LABEL.strip()
    assert label, "label must not be empty"
    assert "\n" not in label, "label must be a single line"
    assert len(label) <= MAX_CHARS, f"label is {len(label)} chars, over {MAX_CHARS}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(label)


if __name__ == "__main__":
    main()
