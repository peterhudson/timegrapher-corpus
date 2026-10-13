# Yacht-Master 42 (cal. 3235), crown right (12 up), about 2.4 h, wound at about 15:30Z

## Reference: tg on this recording
tg is jnarvaezp/tg-mod built with lift angle 55°, run offline (`TG_TRACE=1 xvfb-run -a tg-timer analyze`) on WAVs converted from these FLACs. Its amplitude and beat error are medians of its readings, and its rate is both the median and the mean of its readings. Rate is on the uncalibrated sound-card clock, and beat error is from the unlock. timegrapher is `analyze --lift 55` on main 2045e5e: its rate is a fit over the whole file, and the 10 s window median comes from `--windows`. part01-03 spans the suspend: its audio jumps 1,283 s at 357 s in.

| File | tg amplitude | tg rate, median (s/d) | tg rate, mean (s/d) | tg beat error (ms) | timegrapher amplitude | timegrapher rate, 10 s window median (s/d) | timegrapher rate, whole file (s/d) | timegrapher beat error (ms) |
|---|---|---|---|---|---|---|---|---|
| b_part01-01 | 230° | -9.31 | -10.09 | 0.23 | 235° | -9.4 | -10.6 | 0.23 |
| b_part01-02 | 230° | -10.32 | -10.23 | 0.22 | 235° | -9.9 | -11.8 | 0.22 |
| b_part01-03 | 231° | -6.56 | -9.34 | 0.24 | 236° | -7.0 | -9.6 | 0.22 |
| b_part01-04 | 232° | -6.29 | -8.06 | 0.23 | 237° | -6.6 | -8.4 | 0.22 |
| part01-01 | 228° | -21.19 | -18.73 | 0.22 | 231° | -21.3 | -19.2 | 0.26 |
| part01-02 | 231° | -8.71 | -11.60 | 0.22 | 236° | -9.2 | -11.6 | 0.21 |
| part01-03 | 230° | -10.52 | -11.70 | 0.24 | 234° | -10.4 | -9.9 | 0.19 |
| part01-04 | 230° | -10.50 | -10.51 | 0.24 | 235° | -11.6 | -10.4 | 0.22 |
| part01-05 | 229° | -13.49 | -12.84 | 0.24 | 234° | -13.3 | -14.6 | 0.22 |
| part01-06 | 231° | -10.28 | -10.76 | 0.24 | 235° | -10.4 | -10.3 | 0.22 |
| part01-07 | 230° | -11.63 | -11.95 | 0.23 | 234° | -12.6 | -12.1 | 0.22 |
| part01-08 | 231° | -9.83 | -10.95 | 0.24 | 235° | -10.9 | -11.2 | 0.23 |
| part01-09 | 231° | -9.67 | -10.47 | 0.24 | 235° | -10.2 | -10.4 | 0.22 |

Amplitude reads 3–5° above tg, as in the other positions. Beat error agrees within 0.04 ms except part01-03 (0.19 against 0.24 ms), the file that spans the suspend. Rate agrees within 1.2 s/d like for like (tg's median against timegrapher's window median) in every file, and within 1.8 s/d between tg's mean and timegrapher's whole-file fit (1.6 in part01-05 and b_part01-02, 1.8 in part01-03 across the suspend).

## File names

The audio was renamed to the standard take layout on 2026-10-13 (`take_partPP-NNN`: run, then file;
name order is time order). Notes and tg sources written before then use the old names:

| Old | New |
|---|---|
| `ym42_CR_part01-01.flac` … `ym42_CR_part01-09.flac` | `take_part01-001.flac` … `take_part01-009.flac` |
| `ym42_CR_b_part01-01.flac` … `ym42_CR_b_part01-04.flac` | `take_part02-001.flac` … `take_part02-004.flac` |
