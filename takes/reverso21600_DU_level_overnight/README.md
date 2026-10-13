# JLC Reverso replica (manual wind, 21,600 bph), dial up, level, full wind → 15.8 h run-down

## Reference: tg
tg-mod offline analyze at 21,600 (auto-detected) and lift angle 55°, amplitude scaled by 52/55; engine `timegrapher analyze --lift 52` on main 8ec7b89. Every 8th file (12 of 96, 10 min each), card clock, median and mean of tg's step-3 readings per file (5,841 each; tg's final line is only its last window).

| File (start) | tg rate s/d (median / mean) | Engine rate | tg amp ° | Engine amp ° | tg BE ms | Engine BE ms (unlock) |
|---|---|---|---|---|---|---|
| 01 (0h00) | +18.80 / +18.30 | +18.51 | 259 | 257 | 0.31 | 0.20 |
| 09 (1h20) | +19.42 / +19.41 | +19.41 | 257 | 254 | 0.28 | 0.23 |
| 17 (2h40) | +19.70 / +19.68 | +19.68 | 257 | 255 | 0.21 | 0.25 |
| 25 (4h00) | +19.09 / +19.07 | +19.10 | 258 | 256 | 0.33 | 0.24 |
| 33 (5h20) | +18.96 / +18.78 | +18.76 | 252 | 249 | 0.32 | 0.30 |
| 41 (6h40) | +19.03 / +18.92 | +18.88 | 252 | 250 | 0.39 | 0.27 |
| 49 (8h00) | +18.05 / +17.71 | +17.64 | 251 | 248 | 0.47 | 0.28 |
| 57 (9h20) | +11.30 / +11.70 | +11.65 | 240 | 238 | 0.48 | 0.36 |
| 65 (10h40) | +10.79 / +10.99 | +10.77 | 242 | 239 | 0.42 | 0.35 |
| 73 (12h00) | +11.93 / +11.85 | +11.59 | 243 | 241 | 0.42 | 0.32 |
| 81 (13h20) | +6.30 / +6.54 | +6.51 | 232 | 230 | 0.44 | 0.35 |
| 89 (14h40) | +7.29 / +7.39 | +7.10 | 233 | 232 | 0.43 | 0.34 |

Rate agrees within 0.3 s/d like for like (tg mean vs the engine's whole-file fit; within 0.1 s/d in 8 of 12). Amplitude reads 1–3° below tg in every file (mean 2.3°), a little more than the 0–2° on the 2 h take. Beat error from the unlock reads 0.02–0.19 ms below tg in 11 of 12 files (file 17 is 0.04 above); the 2 h take at Mic 10/16 read above tg instead, so the sign of this gap follows the recording, not a fixed offset. This is the manifest reference for the take: rate is good, amplitude and beat error carry these gaps.

## File names

The audio was renamed to the standard take layout on 2026-10-13 (`take_partPP-NNN`: run, then file;
name order is time order). Notes and tg sources written before then use the old names:

| Old | New |
|---|---|
| `reverso_DUlevel_part01-01.flac` … `reverso_DUlevel_part01-96.flac` | `take_part01-001.flac` … `take_part01-096.flac` |
