# Watch #2: Aquanaut-style case, Dandong Patek 324 clone, dial up, 30 min

## Reference: tg on this recording
tg is jnarvaezp/tg-mod built with lift angle 55°, run offline on these files. Values are medians of its 16 s windows. The 52° column is scaled by 52/55, since the lift angle for this movement isn't settled yet. Rate is on the uncalibrated sound-card clock. Beat error is measured from the unlock.

| Segment | Amplitude @55° | Amplitude @52° | Rate (s/d) | Beat error (ms) |
|---|---|---|---|---|
| -01 | 252° | 238° | −5.01 | 0.41 |
| -02 | 258° | 244° | −5.19 | 0.39 |
| -03 | 260° | 246° | −4.78 | 0.43 |
| **Whole 30 min** | **256°** | **242°** | **−4.98** | **0.41** |

timegrapher (main after PRs #8 and #10, lift 52°) agrees: 243°, −5.1 s/d (window median), beat error from the unlock 0.49 / 0.46 / 0.45 ms against tg's 0.41 / 0.39 / 0.43. The erratic beat errors seen earlier (5.2 and 2.5 ms on segments 01 and 03) came from the beat tracker mixing up tick and tock, which PR #10 fixed. With that fix the once-a-minute rate cycle is 6.7 s/d peak to peak, not the 34.7 s/d reported before. The 18° amplitude cycle every minute is unchanged.

Room AC off for the whole take (the owner's AC log). On the grey USB stand in the dial-up position. Fully wound at the start.

## File names

The audio was renamed to the standard take layout on 2026-10-13 (`take_partPP-NNN`: run, then file;
name order is time order). Notes and tg sources written before then use the old names:

| Old | New |
|---|---|
| `patek324_DU_48000-01.flac` | `take_part01-001.flac` |
| `patek324_DU_48000-02.flac` | `take_part01-002.flac` |
| `patek324_DU_48000-03.flac` | `take_part01-003.flac` |
