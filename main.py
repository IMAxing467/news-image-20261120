"""Entry for make.fun bounty 'Sum up 20 November's world news in one image'.

Writes the news image to /output/entry.png. Deterministic: it copies the
same bundled bytes every run, with no network access.
"""

import shutil
from pathlib import Path

SRC = Path(__file__).with_name("entry.png")
DST = Path("/output/entry.png")


def main() -> None:
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
