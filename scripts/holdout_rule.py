#!/usr/bin/env python3
"""Decide whether a contributed take goes to the holdout tier.

    python3 scripts/holdout_rule.py AUDIO_DIR/TAKE

Run it at import, before anyone listens beyond the privacy check or measures
the take. Of the take's FLAC files, the one whose name sorts first is
hashed; the take is holdout when the first byte of that SHA-256 is below
0x40 (one take in four), otherwise development. The hash is the one
upload.sh records in corpus.json, so anyone can check the assignment later.
Prints "holdout" or "development". Standard library only.
"""
import glob
import hashlib
import os
import sys


def first_byte(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.digest()[0]


def main(argv):
    if len(argv) != 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    files = sorted(glob.glob(os.path.join(argv[1], "*.flac")), key=os.path.basename)
    if not files:
        print(f"no FLAC files in {argv[1]}", file=sys.stderr)
        return 1
    print("holdout" if first_byte(files[0]) < 0x40 else "development")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
