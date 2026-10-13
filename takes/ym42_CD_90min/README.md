# Yacht-Master 42 (cal. 3235), crown down, fully wound just before the start

## Reference: tg on this recording
tg is jnarvaezp/tg-mod built with lift angle 55°, run offline (`TG_TRACE=1 xvfb-run -a tg-timer analyze`) on WAVs converted from these FLACs. Values are medians of its readings. Rate is on the uncalibrated sound-card clock. Beat error is measured from the unlock. Segment 07 is the trimmed 515 s file.

timegrapher is `analyze --lift 55` on main with the burst gate (PRs #29 and #30, the build in PR #30).

| Segment | tg amplitude | tg rate (s/d) | tg beat error (ms) | timegrapher amplitude | timegrapher rate (s/d) | timegrapher beat error (ms) |
|---|---|---|---|---|---|---|
| 01 | 225° | +24.49 | 0.20 | 232° | +25.0 | 0.15 |
| 02 | 231° | +29.14 | 0.24 | 236° | +28.8 | 0.17 |
| 03 | 234° | +38.83 | 0.26 | 239° | +38.4 | 0.18 |
| 04 | 237° | +41.49 | 0.29 | 241° | +41.6 | 0.19 |
| 05 | 235° | +42.82 | 0.22 | 240° | +42.3 | 0.18 |
| 06 | 238° | +44.43 | 0.21 | 241° | +42.7 | 0.20 |
| 07 | 236° | +41.47 | 0.22 | 240° | +40.2 | 0.18 |

Rate agrees within 0.5 s/d in five segments and 1.3–1.7 s/d in the last two, where the rate wanders most. Amplitude reads 3–7° above tg, as on the dial-down take. Beat error reads 0.01–0.10 ms below tg.

the owner's No. 1900 bench timegrapher read +31 s/d and 217° at 52° (about 229° at 55°) crown down at 16:53Z, a few minutes after this take, with its trace moving between +19 and +33 s/d. the owner's by-eye clock readings (+4 s at 15:32Z and at 16:46Z) cannot resolve the predicted gain of about 1.7 s; from now on clock checks are photos of the dial beside a screen clock.

Room AC off for the whole take (the owner's AC log).

## File names

The audio was renamed to the standard take layout on 2026-10-13 (`take_partPP-NNN`: run, then file;
name order is time order). Notes and tg sources written before then use the old names:

| Old | New |
|---|---|
| `ym42_CD_part01-01.flac` … `ym42_CD_part01-07.flac` | `take_part01-001.flac` … `take_part01-007.flac` |
