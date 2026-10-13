# Yacht-Master 42 (cal. 3235), crown up, overnight run (stopped early after 2 h 17 min)

## Reference: tg on this recording
tg is jnarvaezp/tg-mod built with lift angle 55° (the 3235's), run offline on each 10-min file. Values are medians of its 16 s windows; rate on the uncalibrated sound-card clock; beat error from the unlock. timegrapher is `analyze --lift 55` on main with PR #27.

| Segment | tg amplitude | tg rate (s/d) | tg BE (ms) | timegrapher amplitude | timegrapher rate (s/d) | timegrapher BE (ms) |
|---|---|---|---|---|---|---|
| -01 | 221° | −15.53 | 0.28 | 225° | −15.6 | 0.30 |
| -02 | 222° | −16.69 | 0.23 | 223° | −16.0 | 0.21 |
| -03 | 225° | −16.75 | 0.24 | 226° | −16.7 | 0.23 |
| -04 | 224° | −14.50 | 0.21 | 225° | −13.4 | 0.21 |
| -05 | 225° | −12.99 | 0.21 | 227° | −12.2 | 0.22 |
| -06 | 226° | −11.76 | 0.21 | 228° | −11.1 | 0.22 |
| -07 | 227° | −11.56 | 0.21 | 227° | −11.6 | 0.21 |
| -08 | 226° | −11.62 | 0.22 | 226° | −11.2 | 0.21 |
| -09 | 227° | −10.98 | 0.22 | 228° | −10.8 | 0.22 |
| -10 | 226° | −11.53 | 0.23 | 227° | −11.5 | 0.22 |
| -11 | 226° | −11.25 | 0.23 | 227° | −10.7 | 0.22 |
| -12 | 227° | −9.95 | 0.23 | 229° | −9.1 | 0.22 |
| -13 | 227° | −10.41 | 0.24 | 227° | −10.1 | 0.20 |
| -14 | 226° | −10.99 | 0.24 | 227° | −10.7 | 0.22 |

Amplitude within 0–4°, rate within about 1 s/d, beat error within 0.04 ms on every segment: the closest agreement of any take so far.

`timegrapher long --clock clocklog.txt --lift 55 --escape-teeth 20` on the whole take: sound card 21.3 ppm slow, corrected rate **−13.67 s/d**, amplitude 227° (slices 222–230°). No periodic rate change. Amplitude: 60.0 s at 3.2° p-p (fourth wheel; 8° dial up, none found dial down), plus 45.0 s at 3.4° p-p and 54.0 s at 1.9° p-p, and a slow 257 s swing of 4.7°.

Room AC off for the whole take (the owner's AC log).

## File names

The audio was renamed to the standard take layout on 2026-10-13 (`take_partPP-NNN`: run, then file;
name order is time order). Notes and tg sources written before then use the old names:

| Old | New |
|---|---|
| `ym42_CU_48000-01.flac` … `ym42_CU_48000-14.flac` | `take_part01-001.flac` … `take_part01-014.flac` |
