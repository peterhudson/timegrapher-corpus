# Datejust 41 replica, Dandong 3235 movement: ten positions, 1 h 45 min

Example take: it is public and can be fetched by name (`scripts/fetch.py DEST datejust41_3235_multipos_105min`), but `regress` and CI never read it. No checked readings are given here. The app's own last live reading, as the app showed it when the take stopped (in 7H30), is the `result` block at the end of `raw/app_session.json`; it is not a checked reading.

- Recorded with the desktop app (timegrapher-app 1.0.0) as one take, moving the watch through the positions, from 2026-11-18 17:01:42Z to 18:46:46Z. Lift 59° as set in the app, 28,800 bph. 48 kHz, 16-bit mono.
- **Watch:** a 41 mm Datejust "Wimbledon" replica with a Dandong 3235 movement.
- **Complete:** 4 files (`take_part01-001` to `-004`), 6,303.98 s of sound (the app's own duration, and the sum of the files' lengths), 284,548,045 bytes.
- The audio is the app's own `audio-NNN.flac` files, copied byte for byte. `raw/file_map.txt` gives the original names. All four decode without error.
- `raw/app_session.json` and `raw/session.toml` are the app's own session files, unchanged. `clock.csv` is the app's clock log (Unix time against audio frames).
- **Breaks:** the app logged 2 breaks at 1,469.2 s and 1,469.3 s, each with a gap of 0 s and the note "paused". That is why file 002 is only 0.15 s long. All files are kept, so they join as the app recorded them.

## Positions

Each position change is a note in `raw/app_session.json`. `raw/session.toml` lists the stretches the app reads for each position, starting 30 s after each change so the watch can settle. Times are seconds of sound from the start of the take.

| Position | Read from (s) | To (s) | Read (s) |
|---|---:|---:|---:|
| DU | 0.0 | 692.5 | 692.5 |
| DD | 722.5 | 1,372.8 | 650.3 |
| CU | 1,402.8 | 2,073.8 | 671.0 |
| CD | 2,103.8 | 3,069.6 | 965.7 |
| CL | 3,099.6 | 3,709.3 | 609.7 |
| CR | 3,739.3 | 4,425.2 | 685.9 |
| 1H30 | 4,455.2 | 4,717.6 | 262.4 |
| 10H30 | 4,733.3 | 4,733.3 | 0 |
| 4H30 | 4,763.3 | 5,060.9 | 297.6 |
| 7H30 | 5,090.9 | 5,216.7 | 125.8 |
| 10H30 | 5,246.7 | 5,598.0 | 351.3 |
| CR | 5,628.0 | 5,912.6 | 284.6 |
| CL | 5,942.6 | 6,084.2 | 141.6 |
| 7H30 | 6,114.2 | 6,304.0 | 189.8 |

The first 10H30 lasted 15.7 s (from 4,717.6 s to the 4H30 note at 4,733.3 s), shorter than the 30 s settle, so its stretch is empty. 10H30 was recorded again from 5,216.7 s. CR, CL and 7H30 were also recorded a second time at the end.

The take's folder name, "Dial Up", is the app's name for the first position.
