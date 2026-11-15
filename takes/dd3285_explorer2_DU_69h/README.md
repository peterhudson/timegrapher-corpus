# Explorer II replica, Dandong 3285 movement: dial up, 69 h 0 min

Example take: it is public and can be fetched by name (`scripts/fetch.py DEST dd3285_explorer2_DU_69h`), but `regress` and CI never read it. No readings are given here. The take is held out for timegrapher#1817 until a method and its acceptance are posted there.

- Recorded by the owner with the desktop app (timegrapher-app 1.0.1) as one take on the new black stand, from 2026-11-10 06:11:10Z to 11-13 03:11:22Z. It holds 69:00:15 of sound (248,414.9 s) in 84 files, at 48 kHz, 16-bit mono.
- It is the same watch as `dd3285_explorer2_DU_43min_newstand`. Fully wound, dial up. Lift 59° as set in the app, 28,800 bph.
- **Calibre:** the movement is a Dandong 3285. The app's own files in `raw/` say "Dandong 3235", because the app's calibre list offered 3285 only as an alias of the 3235. The owner confirmed the 3285.
- The audio is the app's own `audio-NNN.flac` files, copied byte for byte (each SHA-256 checked against its source). `raw/file_map.txt` gives the original names, and `raw/app_session.json` and `raw/session.toml` are the app's own session files.
- **Breaks:** the app logged 19 breaks, each with a gap of 0 s and the note "paused".
  - 15 come in a burst between 2026-11-10 19:33Z and 21:49Z.
  - 4 come on 11-12, at 16:17Z, 19:28Z, 20:39Z and 23:15Z.
  - Some files between them are only a few kilobytes long (`take_part01-002` among them). All are kept, so the files join as the app recorded them.
- `clock.csv` is the app's clock log for the whole take (Unix time against audio frames).
