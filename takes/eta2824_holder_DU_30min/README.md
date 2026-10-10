# Watch #5: Asian ETA 2824-2 clone, uncased in a plastic movement holder, dial up, 30 min

## Reference: tg on this recording
tg is jnarvaezp/tg-mod built with lift angle 55°, run offline on these files. Values are medians of its 16 s windows. The 50° column (ETA 2824) is scaled by 50/55. Rate is on the uncalibrated sound-card clock. Beat error is measured from the unlock.

| Segment | Amplitude @55° | Amplitude @50° | Rate (s/d) | Beat error (ms) |
|---|---|---|---|---|
| -01 | 324° | 294° | +11.42 | 0.07 |
| -02 | 330° | 300° | +11.33 | 0.09 |
| -03 | 325° | 296° | +11.10 | 0.06 |
| **Whole 30 min** | **327°** | **297°** | **+11.29** | **0.08** |

tg's amplitude is unsteady on this take: its 90th percentile reaches 593–651° in segments 01 and 02.

timegrapher (main, `analyze --lift 50`) per segment:
- amplitude 313° / 298° / 292° (even beats 301 / 297 / 295, odd beats 359 / 322 / 285);
- rate +11.1 / +10.8 / +10.6 s/d;
- beat error from the unlock 0.11 / 0.11 / **2.27** ms (0.19 / 0.69 / 0.67 ms from the drop).

Rate agrees with tg within about 0.4 s/d, and amplitude within about 4°, except segment 01 (19° high, where the odd beats read 359°). Beat error from the unlock is wrong on segment 03. In many 2 s windows one side's amplitude falls outside 100–380°, so that window gets no unlock value, and the few windows that do get one are biased. Only 99 of 299 windows in segment 03 have both sides.

Cause, from the per-side median envelope (`tick_envelope_seg03.png`): in the holder, each tick is a ramp about 7 ms long with no clear gap between the unlock, impulse and drop sounds, and the start of the ramp varies from beat to beat. The plastic holder looks loud but reverberant: it smears the three sounds. So unlock timing (which amplitude and beat error from the unlock depend on) is unreliable. Rate, which only needs the tick times, is unaffected. The bare take on the same movement will show how much of this is the holder.

`timegrapher long --clock clocklog.txt --lift 50 --escape-teeth 20`: the sound card is 32.5 ppm slow, so the corrected rate is **+8.17 s/d**, with amplitude 317° (slices 282–368°).
- Rate cycle: 5.00 s, 63 s/d peak to peak (false alarm 7e-133), which matches the escape wheel.
- Weaker components at 46 s and 60 s, each about 2–3 s/d peak to peak.
- Amplitude cycle: 46 s, false alarm 1e-3, too weak to trust given the amplitude problems above.
