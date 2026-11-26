# Omega 3861 (co-axial escapement), dial up, 10.6 min

Smoke take, contributed by an anonymous user. It is the corpus's first co-axial escapement: an Omega 3861 manual-wind chronograph movement, 21,600 bph, dial up. It is here so the co-axial reading added for timegrapher #2313 runs on a real recording. No reference figures: no tg reading and no paired reading from another instrument.

- **Where it came from:** the contributor's own take, recorded with the desktop app (timegrapher-app 1.1.0) on a commercial timegrapher's pickup, from 2026-11-25 10:29:46Z to 10:40:25Z. The contributor agreed to it being published (2026-11-26, #2313). The pickup's name was removed from `raw/app_session.json`; nothing else in the app's files was changed.
- **The file:** one file, `take_part01-001.flac`, the app's `audio-001.flac` byte for byte (`raw/file_map.txt`; SHA-256 in `corpus.json`): 638.677 s (30,656,512 frames, which is also the last frame count in `clock.csv`), 48 kHz, 16-bit mono, with no tags. It decodes without error.
- `raw/app_session.json` and `raw/app_session.toml.txt` are the app's own session files (the toml renamed so `regress` does not read `raw/` as a session). `clock.csv` is the app's clock log. The app logged one note, "paused", at the end of the take. The app's `result` block is its last live reading at the Swiss-lever setting and 52° default lift; it is not a checked reading.
- **Lift angle:** no checked source gives one for the 3861, so the timegrapher calibre table has none. `session.toml` assumes 36° (`lift_known = false`). At the app's 52° default the Swiss-lever formula puts the amplitude above 400°. Any amplitude read from this take is a co-axial estimate (beta).
- **Escapement:** `session.toml` says `escapement = "co-axial"` and names the calibre, which the table also marks co-axial. On a co-axial, beat error comes from the unlock only.
- **Holdout rule:** `scripts/holdout_rule.py` on this file says development (the SHA-256's first byte is 0x9f), so it is not holdout.
- **Privacy check:** a spectrogram of the whole file shows the ticks and steady tones, with no bursts like speech. It was not listened to by ear at import.
