# Watch #4: Nautilus-style case, Peacock SL1258 (324-like, monolithic bridge), fully wound, dial up, 30 min

## Reference: tg on this recording
tg is jnarvaezp/tg-mod built with lift angle 55°, run offline on these files. Values are medians of its 16 s windows. The 52° column is scaled by 52/55. the owner's bench timegrapher uses 52° for this calibre. Rate is on the uncalibrated sound-card clock. Beat error is measured from the unlock.

| Segment | Amplitude @55° | Amplitude @52° | Rate (s/d) | Beat error (ms) |
|---|---|---|---|---|
| -01 | 323° | 306° | +16.99 | 0.13 |
| -02 | 328° | 310° | +16.62 | 0.14 |
| -03 | 329° | 311° | +17.32 | 0.15 |
| **Whole 30 min** | **327°** | **309°** | **+16.97** | **0.14** |

timegrapher (main after PRs #8 and #10, `analyze --lift 52`) per segment: 307° / 311° / 313°, +17.0 / +16.9 / +17.5 s/d, beat error from the unlock 0.13 / 0.15 / 0.14 ms (0.31 ms from the drop). Its window medians over the whole take are 310° and +16.89 s/d. It agrees with tg within 1° and 0.1 s/d.

`timegrapher long --clock clocklog.txt --lift 52 --escape-teeth 20`: the sound card is 21.8 ppm slow, so the corrected rate is **+15.08 s/d**, with beat error 0.14 ms and amplitude 310° (10 s slices 300–320°).
- Amplitude cycle: 60.03 s, 14.8° peak to peak, explaining 38% of the amplitude variation (false alarm 1e-24), which matches the fourth wheel.
- Rate cycle: 5.00 s, 45.4 s/d peak to peak (false alarm 5e-30), which matches a 20-tooth escape wheel.

So this watch shows the same once-a-minute amplitude dip as the Rolex Yacht-Master and the Patek 324 clone, but not the Dandong 3235 control.
