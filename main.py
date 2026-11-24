#!/usr/bin/env python3
"""One Line, One Chill — writes a single line of horror to /output/entry.txt.

The line: a baby monitor breathing in an empty nursery. The scare is earned,
not announced: a presence that breathes, notices it is being listened to,
and stops.
"""

import os

LINE = "The baby monitor breathed steadily from the empty nursery, and when I held my breath to listen, it stopped."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
