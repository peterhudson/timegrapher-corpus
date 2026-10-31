# JLC Reverso replica (manual wind, unknown movement), DU, 20 min (2026-10-30)

Dial up, on the new black stand (level), Mic 0/16, automatic gain off. Level. Nothing was done to the watch since the 10-10 takes; its rate here matches the owner's bench timegrapher after a run-down (+3 to +7 s/d at 235-245°), so the gap to the grey takes is state of wind or isochronism, not shown to be temperature. Lift 52° as tg (tg's 55° amplitude scaled by 52/55). Rates on the sound card clock, as tg reads them; clock.csv corrects for it. Beat error is from the unlock as tg. Partner take: reverso21600_DU_level_overnight.

## Recording notes

```
Reverso replica (21,600 bph, manual wind), dial up, level on the new black stand, fully wound just before the start. Lift 52 deg.
19:45:26.42Z to 20:05:26Z on 2026-10-30. Mic 0/16, AGC off. 2 x 600 s files.
Grey-cradle partners: reverso21600_DU_2h (tilted cradle) and reverso21600_DU_level_overnight.
Peter 2026-10-30: nothing done to the Reverso since the 10-10 takes (sat on his desk). The ~15 s/d rate difference vs the level overnight grey take is unexplained; candidates are temperature and slight orientation differences.
```

## Reference: tg and timegrapher on this recording

tg is jnarvaezp/tg-mod built at lift 55°, run offline on these files; values are medians of its windows, amplitude at 52°. timegrapher is main 7758065, `analyze --lift 52`. Rates on the sound card clock.

| File | tg amplitude | tg rate (s/d) | tg BE (ms) | timegrapher amplitude | rate | BE |
|---|---|---|---|---|---|---|
| `take_part01-001.flac` | 243° | +3.14 | 0.05 | 245° | +2.00 | 0.00 |
| `take_part01-002.flac` | 245° | +4.65 | 0.05 | 246° | +4.66 | 0.01 |
| **Whole take** | **244°** | **+3.87** | **0.05** | | | |
