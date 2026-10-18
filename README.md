# timegrapher corpus

Recordings of mechanical watches, made with a timegrapher pickup, for testing
[timegrapher](https://github.com/peterhudson/timegrapher). Every take that
has a reference was also read by [tg](https://github.com/vacaboja/tg) on the
same file at the same lift angle, so a change to the engine can be checked
against an independent reading.

## Layout

- `takes/<take>/` holds a take's metadata: `README.md` with tg's readings,
  `session.toml` for `timegrapher session` and `regress`, `session.json`
  (the desktop app's description of a recording: sample rate, start and
  end, the files in order, the logged events, and a break wherever the
  recording stopped and started again), `clock.csv` (the sound card's clock
  log for the whole take, Unix time against frames, with no header line),
  photo-read clock checks (`ground_truth.txt`) where present, and the
  recorder's original logs in `raw/`.
- Audio files are named `take_partPP-NNN.flac`: `PP` is one recording run
  (`02` when a take was carried on in a new run), `NNN` the file within it,
  so name order is time order. Takes recorded before 2026-10-13 had other
  names; each take's README lists them.
- The audio (FLAC, 48 kHz, 16-bit mono) is attached to the release tagged
  `<take>`, not stored in git. `corpus.json` lists every file with its size
  and SHA-256.
- `scripts/fetch.py DEST` downloads and checks the audio, needing nothing
  but Python; it leaves out example and holdout takes unless asked (below).
  `scripts/upload.sh` and `scripts/rename_assets.py` are for maintainers.

## How the takes were recorded

The first takes are one person's bench recordings, 2026-10-08 to 10, with a
C-Media USB timegrapher pickup at 48 kHz, 16-bit mono, automatic gain off
(the mic level is in each take's notes). Takes marked DU on the grey USB
stand are dial up but tilted by its cradle, so their rates differ from a
level reading; the Yacht-Master takes were head only and level, and the
overnight Reverso take was level. Rates in the tg tables are on the sound
card's own clock unless a table says otherwise; `clock.csv` lets you
correct for it. `silence_empty_stand` is the pickup with no watch on it.

## Tiers

- **smoke**: runs through the engine; catches crashes and odd behaviour.
- **referenced**: tg read the same file; numbers are checked against it.
- **paired**: tg plus a commercial timegrapher read at the same time.
- **example**: kept for the documentation's figures and as sample data; no
  tg reference and no `session.toml`, so `regress` never reads it, not even
  with `--smoke`, and none was used to tune the engine. A plain
  `scripts/fetch.py DEST` leaves example takes out; name one to fetch it
  (`scripts/fetch.py DEST TAKE`).
- **holdout**: recordings the engine is never tuned on, read only to check
  it at announced milestones (below).

## The holdout seal

Every smoke, referenced and paired take has been used to tune the engine, so it
cannot show whether the engine works on recordings it has not seen. Holdout
takes are kept apart for that:

- **What goes in.** New recordings only: confirmed faults recorded before
  and after repair, and a share of contributed recordings. None of the
  smoke, referenced or paired takes is holdout: all were used for tuning.
- **How a fault is named.** In a holdout take's `session.toml`, each
  `[[recording]]` entry may carry
  `fault = { id = "...", side = "...", source = "bench: ..." }`. `id` is one
  of timegrapher's fault ids, `side` (Tick, Tock or both) is optional, and
  `source` says how the fault was confirmed. An entry with no `fault` is
  healthy. An entry with a `fault` may leave out `reference`, since tg
  cannot judge a fault.
- **How contributed recordings are assigned.** At import, before anyone
  measures it, `scripts/holdout_rule.py` hashes the take's FLAC file whose
  name sorts first. The take is holdout when the first byte of that SHA-256
  is below `0x40` (one in four), otherwise development. A recording sent in
  with a named fault follows the same rule. The hash is in `corpus.json`, so
  anyone can check the assignment.
- **How they are read.** `scripts/fetch.py` leaves holdout takes out unless
  given `--holdout`, and plain `timegrapher regress` skips them. They are
  measured only by `regress --holdout`, in a manual milestone job that never
  runs on pull requests or pushes and prints pass and fail counts only: no
  take names, file names or numbers.
- **When numbers are shown.** Only at an announced milestone run. Each
  holdout take's README records that run: the engine's git hash, the date
  and the numbers. Between milestones, nobody posts holdout numbers in an
  issue, pull request or discussion, and no engine limit is changed because
  of a holdout result.

The audio is public under CC0 like the rest, so the seal is a convention,
not access control. Please keep to it if you work on the engine.

## Licence

The recordings and metadata are dedicated to the public domain under
[CC0 1.0](LICENSE). This is separate from timegrapher's GPL-3.0 code.
Contributors are credited by handle in a take's README if they wish; a take
is removed on request, though CC0 itself cannot be withdrawn.

## Contributing

Make a bundle with `timegrapher report RECORDING --listened-back --cc0` and
attach it to a *Contribute a recording* issue on
[timegrapher](https://github.com/peterhudson/timegrapher/issues/new/choose).
A maintainer checks the SHA-256 and listens for speech. The maintainer then
assigns the take to holdout or development by the rule above, runs tg on a
development take, and opens the pull request.
