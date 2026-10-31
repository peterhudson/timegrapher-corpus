# Yacht-Master 42 replica, Dandong 3235 movement: dial up, full run-down, 64 h 51 min

Example take: public and fetchable by name (`scripts/fetch.py DEST ym42_DU_65h`), never read by `regress` or CI. Two smoke takes are cut from it: `ym42_DU_65h_excerpt_dying` and `ym42_DU_65h_excerpt_emptystand`.

- Recorded by the owner with the desktop app (0.4.2) as one Quick Listen take on the new black stand, from 2026-10-27 21:19:51Z to 10-30 14:11:00Z. 64:51:11 of sound in 65 files of 3,600 s (the last 3,071.36 s), 48 kHz, 16-bit mono, automatic gain off, app input level 21%.
- The same watch as the `ym42_*` takes. Fully wound, dial up, untouched until it stopped. Lift 55°, 28,800 bph.
- The watch stopped at about 2026-10-30 09:06:42Z, 59.78 h into the take (its last tick in the sound). The last 5 h 4 min is the stand with no watch, kept as a noise sample.
- The audio is the app's `audio-NNN.wav` as FLAC, matched sample for sample against the WAVs. `raw/file_map.txt` gives the original names, and `raw/app_session.json` is the app's own session file.

## Rate from photos (watch dial against the computer's clock)

| Photo (UTC) | Computer | Watch | Watch error | Rate since previous |
|---|---|---|---|---|
| Start, 10-27 | 21:21:53.75 | 21:21:52.0 | −1.75 s | |
| 10-28 | 07:05:51.53 | 07:05:22.4 | −29.13 s | −67.5 s/d over 9 h 44 min |
| 10-29 | 08:14:21.20 | 08:12:28.5 | −112.7 s | −79.8 s/d over 25 h 08 min |
| Stopped, 10-30 | 09:06:42.4 (last tick) | 09:03:34 | −188.4 s | −73.0 s/d over 24 h 52 min |

Start to stop: −186.65 s over 59 h 44 min 49 s, **−75.0 s/d** on the computer's clock. The stopped-dial reading is good to about ±1 s, and its computer time is the last tick in the sound, not a photo.

## Room

`raw/room-temperature.csv` is the room's heat-pump temperature (one row per change, 0.5 °C steps, UTC), 2026-10-25 16:00Z to 10-30 14:09Z. The heat pump is about 1.5 m from the stand. Over the take it reads 19 to 28 °C. The sound card's clock (`clock.csv`) follows it at about −0.24 ppm per °C with a 15 to 30 min lag.
