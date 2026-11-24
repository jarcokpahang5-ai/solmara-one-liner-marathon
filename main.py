"""One-line comedy joke entry for make.fun One-Liner Marathon.

Pure Python 3.13 standard library only. Deterministic, no network.
Writes the joke to /output/entry.txt and prints exactly the same text
to stdout.
"""

import os

JOKE = (
    "My smart fridge filed for divorce - it caught me cheating with "
    "the microwave and says I left it out in the cold."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(JOKE)


if __name__ == "__main__":
    main()
