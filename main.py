"""News-image entry for make.fun news-image-20261118.

The program ships one picture, entry.png, beside this file and hands
a byte-for-byte copy of it to the grader. It does nothing else: no
network, no clock, no randomness, no input besides the file next to
it, so two runs always write the same bytes.

Run it locally the way the grader runs it:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    if not SOURCE.is_file():
        raise FileNotFoundError(f"entry image missing: {SOURCE}")
    if SOURCE.read_bytes()[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry image is not a PNG file")
    shutil.copyfile(SOURCE, target)
    if target.stat().st_size != SOURCE.stat().st_size:
        raise RuntimeError("copied image size differs from the source")


if __name__ == "__main__":
    main()
