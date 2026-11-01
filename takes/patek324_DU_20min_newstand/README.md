# Aquanaut-style case, Dandong 324 clone (bench watch 2), DU, 20 min (2026-10-30)

Dial up, on the new black stand (level), Mic 0/16, automatic gain off. Does not hack. Lift 52° as tg (tg's 55° amplitude scaled by 52/55). Rates on the sound card clock, as tg reads them; clock.csv corrects for it. Beat error is from the unlock as tg. Partner take: patek324_DU_30min.

## Recording notes

```
Dandong 324 clone, dial up, new black stand, fully wound just before the start. Lift 52 deg.
18:32:11.95Z to 18:52:11.98Z on 2026-10-30. Mic 0/16, AGC off, peaks -2.5 dBFS, no clipped samples. 2 x 600 s files.
Quick read (analyze, lift 52, card clock): -20.6 / -18.2 s/d, 237/244 deg, BE 0.49 ms, scatter 0.04%.
Grey-cradle partner: patek324_DU_30min. Its first file, same settings: -6.3 s/d, 240 deg, BE 0.50 ms, scatter 0.063%. Amplitude and BE match; the rate is about 13 s/d slower now (grey cradle tilt, or the regulation or state has changed since).
```

## Reference: tg and timegrapher on this recording

tg is jnarvaezp/tg-mod built at lift 55°, run offline on these files; values are medians of its windows, amplitude at 52°. timegrapher is main 7758065, `analyze --lift 52`. Rates on the sound card clock.

| File | tg amplitude | tg rate (s/d) | tg BE (ms) | timegrapher amplitude | rate | BE |
|---|---|---|---|---|---|---|
| `take_part01-001.flac` | 237° | -20.06 | 0.45 | 237° | -20.60 | 0.49 |
| `take_part01-002.flac` | 243° | -17.56 | 0.44 | 244° | -18.16 | 0.48 |
| **Whole take** | **240°** | **-19.07** | **0.45** | | | |
