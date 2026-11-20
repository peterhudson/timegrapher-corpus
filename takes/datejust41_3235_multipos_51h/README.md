# Datejust 41 replica, Dandong 3235 movement: multi-position, 51 h

Example take: it is public and can be fetched by name (`scripts/fetch.py DEST datejust41_3235_multipos_51h`), but `regress` and CI never read it. No checked readings are given here. The app's own last live reading, as the app showed it when the take stopped (in 7H30), is the `result` block at the end of `raw/app_session.json`; it is not a checked reading.

- Recorded with the desktop app (timegrapher-app 1.0.0) as one take, moving the watch through the positions, from 2026-11-18 18:51:41Z to 2026-11-20 21:46:17Z. Lift 59° as set in the app, 28,800 bph. 48 kHz, 16-bit mono.
- **Watch:** the same 41 mm Datejust "Wimbledon" replica with a Dandong 3235 movement as `datejust41_3235_multipos_105min`, recorded the same day, starting about 5 minutes after that take ended.
- **Shape:** short stretches in seven positions over the first 3.2 h, then four long ones: 4H30 for 17.5 h, DD for 7.2 h, DU for 6.3 h and 7H30 for 16.9 h (time in each position, from one position note to the next).
- **Complete:** 57 files (`take_part01-001` to `-057`), 183,278.08 s of sound (the app's own duration, the sum of the files' lengths, and the last frame count in `clock.csv`: 8,797,347,838 frames), 8,263,720,138 bytes.
- The audio is the app's own `audio-NNN.flac` files, copied byte for byte. `raw/file_map.txt` gives the original names. All 57 decode without error and carry no tags.
- `raw/app_session.json` and `raw/session.toml` are the app's own session files, unchanged. `clock.csv` is the app's clock log (Unix time against audio frames).
- **Breaks:** the app logged 9 breaks, each with a gap of 0 s and the note "paused", at 686.6 s, 7,376.6 s, 77,050.83 s, 77,050.84 s, 100,652.7 s, 101,128.8 s, 124,226.3 s, 124,298.1 s and 172,525.3 s. A new file starts at each one, which is why some files are short (file 024 holds 241 frames, 5 ms). All files are kept, so they join as the app recorded them.

## Positions

Each position change is a note in `raw/app_session.json`. `raw/session.toml` lists the stretches the app reads for each position, starting 30 s after each change so the watch can settle. Times are seconds of sound from the start of the take. The last stretch has no end in `session.toml`; it runs to the end of the take.

| Position | Read from (s) | To (s) | Read (s) |
|---|---:|---:|---:|
| DU | 0.0 | 0.9 | 0.9 |
| CL | 30.9 | 493.4 | 462.6 |
| 4H30 | 499.8 | 499.8 | 0 |
| 7H30 | 529.8 | 713.9 | 184.1 |
| CD | 743.9 | 6,718.4 | 5,974.5 |
| 10H30 | 6,748.4 | 7,527.6 | 779.2 |
| CR | 7,557.6 | 8,235.9 | 678.4 |
| 1H30 | 8,265.9 | 9,889.3 | 1,623.3 |
| CU | 9,919.3 | 11,410.2 | 1,490.9 |
| 4H30 | 11,440.2 | 74,290.2 | 62,850.1 |
| DD | 74,320.2 | 100,068.4 | 25,748.2 |
| DU | 100,098.4 | 122,590.6 | 22,492.2 |
| 7H30 | 122,620.6 | 183,278.1 | 60,657.5 |

The take opened in DU and was moved to CL 0.9 s in, so the first DU stretch holds under a second. The first 4H30 lasted 6.4 s (from 493.4 s to the 7H30 note at 499.8 s), shorter than the 30 s settle, so its stretch is empty. 4H30 was recorded again from 11,410.2 s, for 17.5 h.
