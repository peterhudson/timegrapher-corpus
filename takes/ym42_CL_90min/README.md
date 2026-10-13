# Yacht-Master 42 (cal. 3235), crown left (12 down), 90 min, wound earlier today (full wind at about 15:30Z)

## Reference: tg on this recording
tg is jnarvaezp/tg-mod built with lift angle 55°, run offline (`TG_TRACE=1 xvfb-run -a tg-timer analyze`) on WAVs converted from these FLACs. Its amplitude and beat error are medians of its readings, and its rate is shown both as the median and as the mean of its readings. Rate is on the uncalibrated sound-card clock. Beat error is measured from the unlock.

timegrapher is `analyze --lift 55` on main a6240be. Its rate is a fit over the whole file; the 10 s window median comes from `--windows`.

| Segment | tg amplitude | tg rate, median (s/d) | tg rate, mean (s/d) | tg beat error (ms) | timegrapher amplitude | timegrapher rate, 10 s window median (s/d) | timegrapher rate, whole file (s/d) | timegrapher beat error (ms) |
|---|---|---|---|---|---|---|---|---|
| 01 | 233° | +71.22 | +67.21 | 0.21 | 236° | +71.5 | +66.5 | 0.19 |
| 02 | 232° | +70.64 | +68.23 | 0.20 | 236° | +71.0 | +68.2 | 0.21 |
| 03 | 233° | +75.74 | +70.26 | 0.19 | 236° | +75.8 | +70.0 | 0.22 |
| 04 | 232° | +72.89 | +67.70 | 0.13 | 234° | +73.0 | +67.0 | 0.16 |
| 05 | 230° | +72.50 | +65.87 | 0.10 | 234° | +72.6 | +66.4 | 0.13 |
| 06 | 230° | +65.46 | +63.61 | 0.10 | 233° | +66.2 | +66.4 | 0.11 |
| 07 | 230° | +73.71 | +67.63 | 0.10 | 234° | +74.3 | +68.8 | 0.10 |
| 08 | 230° | +76.78 | +71.09 | 0.09 | 235° | +76.5 | +71.2 | 0.11 |
| 09 | 227° | +61.25 | +59.45 | 0.07 | 232° | +60.7 | +57.2 | 0.07 |

Crown left, the rate wanders between about +35 and +85 s/d within each 10 minutes, with dips downward, so the median reading sits 2–6 s/d above the average. Compared like for like, the two programs agree: tg's median against timegrapher's window median is within 0.6 s/d in every segment, and tg's mean against timegrapher's whole-file fit is within 0.7 s/d in seven of the nine segments (2.8 s/d in 06, which has a clipped knock, and 2.3 s/d in 09). Amplitude reads 2–5° above tg, as on the other Yacht-Master positions. Beat error agrees within 0.03 ms.

For a watch whose rate wanders like this, the average (tg's mean, timegrapher's whole-file rate) is what the hands keep, so it is what to compare with the clock photos.

## File names

The audio was renamed to the standard take layout on 2026-10-13 (`take_partPP-NNN`: run, then file;
name order is time order). Notes and tg sources written before then use the old names:

| Old | New |
|---|---|
| `ym42_CL_part01-01.flac` … `ym42_CL_part01-09.flac` | `take_part01-001.flac` … `take_part01-009.flac` |
