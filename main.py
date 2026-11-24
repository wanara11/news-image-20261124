# news-image-20261124 entry: one image summing up Tuesday 24 November 2026.
#
# The entry is the entry.png beside this file (a JPEG image, which the gate
# accepts under the entry.png name). This program copies it, byte for byte,
# to the output directory the grader reads: /output/entry.png, or
# $MAKEFUN_OUTPUT_DIR/entry.png when run outside the grader's container.
#
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# Standard library only, no network, deterministic: two runs write the
# same bytes.

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dst = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    # Self-check: the copy must be the same size as the source, so a
    # truncated write fails loudly instead of entering a broken image.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit("copy size mismatch")
    return 0


if __name__ == "__main__":
    sys.exit(main())
