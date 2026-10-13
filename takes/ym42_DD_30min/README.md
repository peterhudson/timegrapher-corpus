# Yacht-Master 42 (cal. 3235), dial down, 30 min

## Reference: tg on this recording
tg is jnarvaezp/tg-mod built with lift angle 55° (the 3235's), run offline on these files. Values are medians of its 16 s windows. Rate is on the uncalibrated sound-card clock. Beat error is measured from the unlock.

| Segment | Amplitude @55° | Rate (s/d) | Beat error (ms) |
|---|---|---|---|
| -01 | 235° | +46.83 | 0.25 |
| -02 | 236° | +48.14 | 0.20 |
| -03 | 229° | +26.63 | 0.19 |

timegrapher (`analyze --lift 55`, main with PR #27 "Keep the beat count through a loud knock"): amplitude 241° / 240° / 233°, rate +43.3 / +46.9 / +28.2 s/d, beat error from the unlock 0.00 / 0.03 / 0.21 ms (0.71 / 0.15 / 0.29 ms from the drop). Without #27, segment 01 read +34,553 s/d and 174°: two full-scale knocks at 180.0 s and 181.9 s threw the beat count off. Amplitude reads 4–6° above tg. The rate wanders widely within each segment (10 s windows from about +17 to +59 s/d), so tg's median of windows and the engine's whole-segment fit differ by up to 3.5 s/d. Beat error from the unlock reads low on 01 and 02.

Room AC off for the whole take (the owner's AC log).

## File names

The audio was renamed to the standard take layout on 2026-10-13 (`take_partPP-NNN`: run, then file;
name order is time order). Notes and tg sources written before then use the old names:

| Old | New |
|---|---|
| `ym42_DD_48000-01.flac` | `take_part01-001.flac` |
| `ym42_DD_48000-02.flac` | `take_part01-002.flac` |
| `ym42_DD_48000-03.flac` | `take_part01-003.flac` |
