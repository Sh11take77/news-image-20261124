"""Sum up 24 November 2026 world news in one image.

Deterministic, offline program for make.fun bounty
news-image-20261124. It copies the pre-made infographic
image.png (1024x1024 PNG, 901,171 bytes) to
/output/entry.png, byte-for-byte, so two runs produce
identical output.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "image.png")
OUT = "/output/entry.png"


def main() -> int:
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, OUT)
    print(f"Wrote {OUT} ({os.path.getsize(OUT)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
