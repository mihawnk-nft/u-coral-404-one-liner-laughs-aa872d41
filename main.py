"""One-Liner Laughs - make.fun u-coral-404-one-liner-laughs-aa872d41 entry.

Writes one original one-line joke to /output/entry.txt.
Pure stdlib, no network, fully deterministic.
"""

import os

JOKE = (
    "I asked my GPS for the meaning of life. It paused, then said, "
    "'Recalculating' \u2014 which honestly explains my twenties."
)

DST = "/output/entry.txt"


def main():
    text = JOKE
    if not (1 <= len(text) <= 200):
        raise ValueError("joke must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("joke must not be only whitespace")
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote %s (%d chars)" % (DST, len(text)))


if __name__ == "__main__":
    main()
