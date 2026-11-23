#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh — make.fun entry.

Writes one safety warning label (max 160 characters) for every human
being to /output/entry.txt. Stdlib only, no network, no dependencies.

Run: python3 main.py
"""

import os

LINE = (
    "WARNING: This human checks the fridge twice, knowing nothing new "
    "has appeared since the first check."
)


def main() -> None:
    # Fail loudly instead of shipping an entry the gate would refuse:
    # 1-160 UTF-8 characters, not whitespace-only, exactly one line.
    if not LINE.strip():
        raise SystemExit("entry line is empty or whitespace-only")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry line must be a single line")
    if not 1 <= len(LINE) <= 160:
        raise SystemExit(f"entry line is {len(LINE)} characters, must be 1-160")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
