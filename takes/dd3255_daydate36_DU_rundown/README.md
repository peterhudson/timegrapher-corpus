# Day-Date 36 replica, Dandong 3255 movement: dial up, run-down (partial, still recording)

Example take: it is public and can be fetched by name (`scripts/fetch.py DEST dd3255_daydate36_DU_rundown`), but `regress` and CI never read it. No readings are given here. The take is held out for timegrapher#1817 until a method and its acceptance are posted there. It is also the take behind timegrapher#1819 (beat error flipping in Live).

- Recorded with the desktop app (timegrapher-app 1.0.0) as one take, dial up, starting 2026-11-14 05:45:12Z, letting the watch run down. Lift 59° as set in the app, 28,800 bph. 48 kHz, 16-bit mono.
- **Partial:** this release holds the first 92 files (`take_part01-001` to `-092`), 130,964 s (36.4 h) of sound, up to 2026-11-15 18:07:55Z. The take was still recording when they were uploaded. Later files will be added to the same release, and this README updated, once the take is stopped.
- **Calibre:** the movement is a Dandong 3255 (day and date). The app's own files in `raw/` say "Dandong 3235", because the app's calibre list offered 3255 only as an alias of the 3235.
- The audio is the app's own `audio-NNN.flac` files, copied byte for byte (each SHA-256 checked against its source). `raw/file_map.txt` gives the original names.
- `raw/app_session.json` and `raw/session.toml` are the app's own session files, copied part way through the take, so they list 96 segments (93 to 96 are not in this release yet). The only change is the watch name, shortened to "DayDate 36". The owner's watch file is not published.
- **Breaks:** the app's log so far holds 63 breaks, each with a gap of 0 s and the note "paused". All files are kept, so they join as the app recorded them.
- `clock.csv` is the app's clock log (Unix time against audio frames), copied at the same moment as the session files.
