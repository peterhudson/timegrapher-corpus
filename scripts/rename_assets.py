#!/usr/bin/env python3
"""Maintainer only: rename the release audio to the standard take layout.

    python3 scripts/rename_assets.py [--apply] [TAKE ...]

On 2026-10-13 every take's audio was renamed to take_partPP-NNN.flac (PP
the recording run, NNN the file in it, so name order is time order).
corpus.json and takes/<take>/ carry the new names; this renames the files
attached to each take's release to match, from scripts/renames-2026-10.json.
The files themselves do not change, so their SHA-256 in corpus.json stays.
A file that already has its new name is skipped, so it can be run again.
Without --apply it only prints what it would rename. Needs gh with push
access to this repository.
"""
import json
import os
import subprocess
import sys

REPO = "peterhudson/timegrapher-corpus"
HERE = os.path.dirname(os.path.abspath(__file__))


def main(argv):
    apply = "--apply" in argv
    wanted = {a for a in argv[1:] if not a.startswith("--")}
    with open(os.path.join(HERE, "renames-2026-10.json")) as f:
        renames = json.load(f)
    done = 0
    for take, names in renames.items():
        if wanted and take not in wanted:
            continue
        out = subprocess.run(
            ["gh", "api", f"repos/{REPO}/releases/tags/{take}", "--jq", '.assets[] | "\\(.id) \\(.name)"'],
            capture_output=True, text=True, check=True).stdout
        have = dict(line.split(" ", 1)[::-1] for line in out.splitlines() if line)
        for old, new in names.items():
            if new in have and old not in have:
                continue
            if old not in have:
                print(f"{take}: {old} is not attached", file=sys.stderr)
                continue
            print(f"{take}: {old} -> {new}" + ("" if apply else " (dry run)"))
            if apply:
                subprocess.run(["gh", "api", "-X", "PATCH", f"repos/{REPO}/releases/assets/{have[old]}",
                                "-f", f"name={new}", "--silent"], check=True)
            done += 1
    print(f"{done} file(s) {'renamed' if apply else 'to rename; add --apply'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
