# Day-Date 36 replica, Dandong 3255 movement: dial up, run-down (partial, still recording)

Example take: it is public and can be fetched by name (`scripts/fetch.py DEST dd3255_daydate36_DU_rundown`), but `regress` and CI never read it. No checked readings are given here. The app's own last live reading, as the app showed it when the file was saved, is the `result` block at the end of `raw/app_session.json`; it is not a checked reading. The take is held out for timegrapher#1817 until a method and its acceptance are posted there. It is also the take behind timegrapher#1819 (beat error flipping in Live). Files 093 onward are held out from that work too, for testing its method once Norm signs it off on #1819.

- Recorded with the desktop app (timegrapher-app 1.0.0) as one take, dial up, starting 2026-11-14 05:45:12Z, letting the watch run down. Lift 59° as set in the app, 28,800 bph. 48 kHz, 16-bit mono.
- **Partial:** this release holds the first 112 files (`take_part01-001` to `-112`), 148,570 s (41.3 h) of sound, up to 2026-11-15 23:01:22Z. Files 001 to 092 were added at 18:39Z and 093 to 112 at 23:40Z on 2026-11-15, while the take was still recording. Later files will be added to the same release, and this README updated, once the take is stopped.
- **Calibre:** the movement is a Dandong 3255 (day and date). The app's own files in `raw/` say "Dandong 3235", because the app's calibre list offered 3255 only as an alias of the 3235.
- The audio is the app's own `audio-NNN.flac` files, copied byte for byte (each SHA-256 checked against its source). `raw/file_map.txt` gives the original names.
- `raw/app_session.json` and `raw/session.toml` are the app's own session files, copied part way through the take (at 2026-11-15 23:33Z), so they list 113 segments (113 is not in this release yet). The only change is the watch name, shortened to "DayDate 36". The owner's watch file is not published.
- **Breaks:** the app's log so far holds 76 breaks, each with a gap of 0 s and the note "paused". All files are kept, so they join as the app recorded them.
- `clock.csv` is the app's clock log (Unix time against audio frames), copied at the same moment as the session files.
