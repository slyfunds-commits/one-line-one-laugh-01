"""One Line, One Laugh — writes the keeper line to /output/entry.txt.

Pure Python standard library only (the grader runs python:3.13-slim with no
site-packages). Deterministic: the same 69 bytes on every run, no trailing
newline.
"""

import os

KEEPER = "My son's report says 'easily distracted'. It took 11 pages to say it."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(KEEPER)


if __name__ == "__main__":
    main()
