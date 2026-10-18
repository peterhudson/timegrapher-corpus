#!/bin/bash
# Maintainer only: attach a take's audio to its release and record the
# files in corpus.json.
#
#   scripts/upload.sh AUDIO_DIR TAKE [TIER]
#
# TIER is smoke, referenced, paired, example or holdout; it defaults to the
# take's tier in corpus.json, or referenced for a new take.
# AUDIO_DIR/TAKE/*.flac are uploaded to the release tagged TAKE (created if
# missing); files already attached are skipped. corpus.json gets the take's
# entry with each file's size and SHA-256. Commit corpus.json and
# takes/TAKE/ afterwards. For a contributed take, run
# scripts/holdout_rule.py AUDIO_DIR/TAKE first and pass holdout when it
# says so. Needs gh with push access to this repository.
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
audio="$1"; take="$2"; tier="${3:-}"
[ -d "$here/takes/$take" ] || { echo "takes/$take/ is missing: add its metadata first" >&2; exit 1; }
shopt -s nullglob
files=("$audio/$take"/*.flac)
[ ${#files[@]} -gt 0 ] || { echo "no FLAC files in $audio/$take" >&2; exit 1; }

repo=peterhudson/timegrapher-corpus
gh release view "$take" -R "$repo" >/dev/null 2>&1 ||
  gh release create "$take" -R "$repo" --title "$take" \
    --notes "Audio for takes/$take. CC0 1.0. See takes/$take/README.md."
have="$(gh release view "$take" -R "$repo" --json assets --jq '.assets[].name')"
for f in "${files[@]}"; do
  n="$(basename "$f")"
  if grep -qxF "$n" <<<"$have"; then echo "already attached: $n"; continue; fi
  gh release upload "$take" -R "$repo" "$f"
done

python3 - "$here/corpus.json" "$take" "$tier" "${files[@]}" <<'PY'
import hashlib, json, os, sys
path, take, tier, files = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]
def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()
corpus = json.load(open(path)) if os.path.exists(path) else {"schema": 1, "takes": []}
old = {t["id"]: t for t in corpus["takes"]}.get(take, {})
tier = tier or old.get("tier", "referenced")
entry = {"id": take, "tier": tier, "release": take,
         "files": [{"name": os.path.basename(f), "bytes": os.path.getsize(f), "sha256": sha(f)}
                   for f in sorted(files)]}
corpus["takes"] = sorted([t for t in corpus["takes"] if t["id"] != take] + [entry],
                         key=lambda t: t["id"])
with open(path, "w") as f:
    json.dump(corpus, f, indent=1)
    f.write("\n")
print(f"corpus.json: {take}, {len(files)} files")
PY
