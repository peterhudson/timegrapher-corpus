# Daytona case, Dandong 4130 clone with genuine balance, free sprung, not regulated (bench watch 1, the Black Dial Daytona), DU, 20 min (2026-10-30)

Dial up, on the new black stand (level), Mic 0/16, automatic gain off. The same watch as daytona4130_DU_30min. Lift 55° as tg. Rates on the sound card clock, as tg reads them; clock.csv corrects for it. Beat error is from the unlock as tg. Partner take: daytona4130_DU_30min.

## Recording notes

```
Black-dial Daytona (Dandong 4130 with a genuine free-sprung balance), dial up, new black stand, fully wound just before the start. Lift 52 deg.
18:09:48.92Z to 18:29:48.94Z on 2026-10-30. Mic 0/16, AGC off, peaks -0.6 dBFS, no clipped samples. 2 x 600 s files.
Quick read (analyze, lift 52, card clock): +3.7 / +3.3 s/d, 307/309 deg, BE 0.18 ms, scatter 0.06%.
Grey-cradle partner: daytona4130_DU_30min (the owner confirmed it is the same watch). Its first 10 min, same settings: +6.2 s/d, 303 deg, BE 0.35 ms, scatter 0.086%.
```

## Reference: tg and timegrapher on this recording

tg is jnarvaezp/tg-mod built at lift 55°, run offline on these files; values are medians of its windows, amplitude at 55°. timegrapher is main 7758065, `analyze --lift 55`. Rates on the sound card clock.

| File | tg amplitude | tg rate (s/d) | tg BE (ms) | timegrapher amplitude | rate | BE |
|---|---|---|---|---|---|---|
| `take_part01-001.flac` | 325° | +3.69 | 0.32 | 324° | +3.69 | 0.18 |
| `take_part01-002.flac` | 327° | +3.38 | 0.31 | 326° | +3.33 | 0.18 |
| **Whole take** | **326°** | **+3.52** | **0.31** | | | |
