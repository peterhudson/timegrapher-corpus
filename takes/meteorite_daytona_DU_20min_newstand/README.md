# Meteorite-dial Daytona case, Dandong 4130 clone, regulated, DU, 20 min (2026-10-30)

Dial up, on the new black stand (level), Mic 0/16, automatic gain off. A second 4130 Daytona, not the watch of daytona4130_DU_30min. Lift 55° as tg. Rates on the sound card clock, as tg reads them; clock.csv corrects for it. Beat error is from the unlock as tg. Partner take: meteorite_daytona_DU_75min.

## Recording notes

```
Meteorite Daytona (Dandong 4130), dial up, new black stand, fully wound just before the start. Lift 52 deg (corpus value for the 4130).
17:47:21.65Z to 18:07:21.74Z on 2026-10-30. Mic 0/16, AGC off, peaks -4.3 dBFS, no clipping. 2 x 600 s files.
Quick read (analyze, lift 55, card clock): 10 min files +6.5 / +8.6 s/d, 308/304 deg at lift 55 (about 291/287 at 52), BE 0.03 ms, scatter 0.06%.
Grey-cradle partner: meteorite_daytona_DU_40h.
```

## Reference: tg and timegrapher on this recording

tg is jnarvaezp/tg-mod built at lift 55°, run offline on these files; values are medians of its windows, amplitude at 55°. timegrapher is main 7758065, `analyze --lift 55`. Rates on the sound card clock.

| File | tg amplitude | tg rate (s/d) | tg BE (ms) | timegrapher amplitude | rate | BE |
|---|---|---|---|---|---|---|
| `take_part01-001.flac` | 301° | +6.47 | 0.01 | 308° | +6.54 | 0.03 |
| `take_part01-002.flac` | 303° | +8.58 | 0.01 | 304° | +8.58 | 0.03 |
| **Whole take** | **302°** | **+7.76** | **0.01** | | | |
