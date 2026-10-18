# Pepsi (Dandong 3235 clone), dial up, 7 h 28 min

- Recorded by the owner with the desktop app (timegrapher-app 0.4.2) on 2026-10-17, from **21:32:19.851Z to 05:00:44.686Z (10-18)**: **26,904.19 s in one continuous run**, no breaks. 48 kHz, 16-bit mono, through PipeWire's default input (the C-Media USB timegrapher pickup).
- Calibre Dandong 3235 (28,800 bph), lift angle 55°. **Dial up in the grey USB cradle** (not stated as levelled; on that cradle DU can be slightly tilted, see the corpus README). **Fully wound** at the start.
- Room (owner's notes): a little AC at the start, otherwise a very quiet take; nobody talking nearby (owner home alone, silent all day).
- Files: `take_part01-001.flac` … `-007.flac` (1 h each) and `-008.flac` (1,704.19 s). The app saved them as `audio-001.wav` … `audio-008.wav`; `raw/` holds the app's original `session.json` and `session.toml` with those names.
- `clock.csv` is the app's clock log (Unix time against frames, every 10 s, 2,684 rows, no gaps). It puts the sound card **21.64 ppm slow** (about 1.87 s/d), the same as the earlier takes on this pickup.
- The app's reading at the end of the take (last 10 s, in `session.json` → `result`): +13.1 s/d (card clock), 225° (tick 222°, tock 230°), beat error 0.75 ms (0.40 ms from the unlock), SNR 16, no clipping.
- **Tier: smoke** (no tg reference yet). **Holdout rule: development.** `scripts/holdout_rule.py` on `take_part01-001.flac` gives SHA-256 first byte 0x7e (≥ 0x40), run before the take was measured by anyone other than the app's live display.
- Added for the user guide's automated screenshots, and as a long single-run take from the app's own recorder.
