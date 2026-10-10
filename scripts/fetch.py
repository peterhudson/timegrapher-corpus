#!/usr/bin/env python3
"""Download the corpus audio from this repository's releases and check it.

    python3 scripts/fetch.py DEST [TAKE ...]

Each take's audio is attached to the release tagged with the take's name.
Files land in DEST/<take>/<file>, next to a copy of the take's metadata, so
`timegrapher regress DEST` sees the same layout as the private recordings.
A file already present with the right SHA-256 is not downloaded again.
Standard library only, so it runs on any CI runner with no secret.
"""
import hashlib
import json
import os
import shutil
import sys
import urllib.request

REPO = "peterhudson/timegrapher-corpus"
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def main(argv):
    if len(argv) < 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    dest, wanted = argv[1], set(argv[2:])
    with open(os.path.join(HERE, "corpus.json")) as f:
        corpus = json.load(f)
    bad = 0
    for take in corpus["takes"]:
        name = take["id"]
        if wanted and name not in wanted:
            continue
        out = os.path.join(dest, name)
        shutil.copytree(os.path.join(HERE, "takes", name), out, dirs_exist_ok=True)
        for f in take["files"]:
            path = os.path.join(out, f["name"])
            if os.path.exists(path) and sha256(path) == f["sha256"]:
                continue
            url = f"https://github.com/{REPO}/releases/download/{take['release']}/{f['name']}"
            print(f"{name}/{f['name']} ({f['bytes'] / 1e6:.0f} MB)", flush=True)
            with urllib.request.urlopen(url) as r, open(path + ".part", "wb") as w:
                shutil.copyfileobj(r, w, 1 << 20)
            os.replace(path + ".part", path)
            if sha256(path) != f["sha256"]:
                print(f"  SHA-256 mismatch: {path}", file=sys.stderr)
                bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
