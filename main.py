"""One Line, One Laugh — Task 9 entry.

Writes a single funny line of text to /output/entry.txt.

The line is a self-contained joke: a school report calls the boy
"easily distracted", and the report itself takes eleven pages to
say so — the evidence convicts the accuser. The number is the
punch mechanism, not decoration: eleven pages to deliver a
two-word verdict is the joke doing the work.
"""

import os

ENTRY = "My son's report says 'easily distracted'. It took 11 pages to say it."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
