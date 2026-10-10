# timegrapher corpus

Recordings of mechanical watches, made with a timegrapher pickup, for testing
[timegrapher](https://github.com/peterhudson/timegrapher). Every take that
has a reference was also read by [tg](https://github.com/vacaboja/tg) on the
same file at the same lift angle, so a change to the engine can be checked
against an independent reading.

## Layout

- `takes/<take>/` holds a take's metadata: `README.md` with tg's readings,
  `session.toml` for `timegrapher session` and `regress`, and where present
  the sound card's clock log (`clocklog.txt`) and photo-read clock checks
  (`ground_truth.txt`).
- The audio (FLAC, 48 kHz, 16-bit mono) is attached to the release tagged
  `<take>`, not stored in git. `corpus.json` lists every file with its size
  and SHA-256.
- `scripts/fetch.py DEST` downloads and checks the audio, needing nothing
  but Python. `scripts/upload.sh` is for maintainers.

## Tiers

- **smoke**: runs through the engine; catches crashes and odd behaviour.
- **referenced**: tg read the same file; numbers are checked against it.
- **paired**: tg plus a commercial timegrapher read at the same time.

## Licence

The recordings and metadata are dedicated to the public domain under
[CC0 1.0](LICENSE). This is separate from timegrapher's GPL-3.0 code.
Contributors are credited by handle in a take's README if they wish; a take
is removed on request, though CC0 itself cannot be withdrawn.

## Contributing

Make a bundle with `timegrapher report --kind contribution` and attach it to
an issue here, with the corpus box ticked. A maintainer checks the SHA-256,
listens for speech, runs tg, and opens the pull request.
