# JLC Reverso replica (manual wind, unknown movement), 21,600 bph, dial up, about 2 h 4 min

## Reference: tg
tg-mod offline analyze at 21,600 (auto-detected) and lift angle 55°, amplitude scaled by 52/55; engine `timegrapher analyze --lift 52` on main 95bb92a. Card clock, per file, median of tg's step-3 readings.

| File | tg rate s/d (median / mean) | Engine rate | tg amp ° | Engine amp ° | tg BE ms | Engine BE ms (unlock) |
|---|---|---|---|---|---|---|
| 01 | +22.60 / +22.00 | +21.9 | 238 | 239 | 0.33 | 0.36 |
| 02 | +23.69 / +23.60 | +23.7 | 245 | 247 | 0.30 | 0.34 |
| 03 | +22.74 / +22.71 | +22.7 | 251 | 252 | 0.31 | 0.34 |
| 04 | +22.51 / +22.50 | +22.5 | 255 | 256 | 0.34 | 0.36 |
| 05 | +22.53 / +22.61 | +22.6 | 258 | 258 | 0.33 | 0.38 |
| 06 | +22.43 / +22.50 | +22.4 | 252 | 252 | 0.35 | 0.41 |
| 07 | +21.59 / +21.60 | +21.7 | 250 | 250 | 0.29 | 0.42 |
| 08 | +20.84 / +20.82 | +20.8 | 252 | 251 | 0.29 | 0.41 |
| 09 | +20.56 / +20.49 | +20.5 | 249 | 248 | 0.29 | 0.40 |
| 10 | +20.73 / +20.74 | +20.7 | 251 | 249 | 0.25 | 0.39 |
| 11 | +21.15 / +21.05 | +21.2 | 252 | 251 | 0.25 | 0.38 |
| 12 | +21.45 / +21.41 | +21.4 | 246 | 246 | 0.31 | 0.43 |
| 13 | +20.94 / +20.57 | +20.7 | 245 | 243 | 0.27 | 0.43 |

Rate agrees within 0.4 s/d like for like (tg mean vs the engine's whole-file fit, 0.1 s/d in 12 of 13), amplitude within 2°: the first 21,600 watch matches tg as closely as the best 28,800 takes. Beat error reads 0.03–0.14 ms above tg, more in files 07–13 (clipping from file 02 on, Mic 10/16, may shift the unlock edge; a check for the research thread).

## File names

The audio was renamed to the standard take layout on 2026-10-13 (`take_partPP-NNN`: run, then file;
name order is time order). Notes and tg sources written before then use the old names:

| Old | New |
|---|---|
| `reverso_DU_part01-01.flac` … `reverso_DU_part01-13.flac` | `take_part01-001.flac` … `take_part01-013.flac` |
