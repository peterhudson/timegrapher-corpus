# Watch #5: ETA 2824-2 clone, bare movement (no holder), dial up, 30 min at Mic 10/16

## Reference: tg on this recording
tg is jnarvaezp/tg-mod built with lift angle 55°, run offline on these files. Values are medians of its 16 s windows. The 50° column (ETA 2824) is scaled by 50/55. Rate is on the uncalibrated sound-card clock. Beat error is measured from the unlock.

| Segment | Amplitude @55° | Amplitude @50° | Rate (s/d) | Beat error (ms) |
|---|---|---|---|---|
| -01 | 307° | 279° | +10.78 | 0.32 |
| -02 | 311° | 283° | +11.04 | 0.33 |
| -03 | 309° | 281° | +10.71 | 0.29 |
| **Whole 30 min** | **309°** | **281°** | **+10.85** | **0.31** |

tg is steady on this take (90th percentile 315–324° at 55°), unlike the holder take, where it reached 593–651°.

timegrapher (main, `analyze --lift 50`) per segment:
- amplitude 297° / 299° / 293° (Tick 304 / 307 / 288, Tock 286 / 291 / 294);
- rate +10.8 / +11.1 / +10.8 s/d;
- beat error from the unlock 0.23 / 0.19 / 0.17 ms (0.26 / 0.31 / 0.22 ms from the drop).

Rate agrees with tg within 0.1 s/d. Amplitude reads 14–18° high, the largest gap on any tg-grounded take so far (the others agree within 3–4°). Beat error from the unlock reads 0.09–0.14 ms low. On the median tick at 300 s of the Mic 4/16 take the engine times the unlock about 8 ms before the drop on both sides; an amplitude 16° lower needs that interval about 0.2 ms longer, so one of the two edges is placed a little differently from tg's. Under investigation in the research thread.

This take clips (see above), but the unclipped Mic 4/16 take that follows shows the same gap (engine 296°, tg 276°), so clipping does not explain it.

Room AC off for the whole take (the owner's AC log).

## File names

The audio was renamed to the standard take layout on 2026-10-13 (`take_partPP-NNN`: run, then file;
name order is time order). Notes and tg sources written before then use the old names:

| Old | New |
|---|---|
| `eta2824_bare_DU_48000-01.flac` | `take_part01-001.flac` |
| `eta2824_bare_DU_48000-02.flac` | `take_part01-002.flac` |
| `eta2824_bare_DU_48000-03.flac` | `take_part01-003.flac` |
