# Pepsi (Dandong 3235 clone), dial up, 7 h 28 min

- Recorded by the owner with the desktop app (timegrapher-app 0.4.2) on 2026-10-17, from **21:32:19.851Z to 05:00:44.686Z (10-18)**: **26,904.19 s in one continuous run**, no breaks. 48 kHz, 16-bit mono, through PipeWire's default input (the C-Media USB timegrapher pickup).
- The app was set to calibre Dandong 3235 (28,800 bph) and a lift angle of 55° for this recording (the calibre table's 55° comes from a QC guide and may not be exact). **Dial up in the grey USB cradle** (not stated as levelled; on that cradle DU can be slightly tilted, see the corpus README). **Fully wound** at the start.
- Room (owner's notes): a little AC at the start, otherwise a very quiet take; nobody talking nearby. A screen of the voice band (150 to 3,400 Hz, the median of each second against the file's own level) found no stretch of two seconds or more above +8 dB in any file; the loudest second, `take_part01-004.flac` at 1,663 s, is a tap or bump on the stand that clips for about 0.3 s.
- Files: `take_part01-001.flac` … `-007.flac` (1 h each) and `-008.flac` (1,704.19 s). The app saved them as `audio-001.wav` … `audio-008.wav` (table below); `raw/` holds the app's original `session.json`, and its `session.toml` renamed `app_session.toml.txt`, with those names. The top-level `session.json` has the new names, the beat rate filled in, and no `device` field (as in the other takes).
- `clock.csv` is the app's clock log (Unix time against frames, every 10 s, 2,684 rows, no gaps; its two header lines removed, as in the other takes). It puts the sound card **21.64 ppm slow** (about 1.87 s/d), the same as the earlier takes on this pickup.
- The app's reading at the end of the take (last 10 s, in `session.json` → `result`): +13.1 s/d (card clock), 225° (tick 222°, tock 230°), beat error 0.75 ms (0.40 ms from the unlock), SNR 16, no clipping.
- **Tier: example** (no tg reference; kept for the user guide's figures, so `regress` never reads it). The take has no `session.toml`, like `silence_empty_stand`; the app's settings were calibre Dandong 3235, lift 55°, dial up, `clock.csv` for the clock. **Holdout rule: development.** `scripts/holdout_rule.py` on `take_part01-001.flac` gives SHA-256 first byte 0x7e (≥ 0x40), run before the take was measured by anyone other than the app's live display.
- Added for the user guide's automated screenshots, and as a long single-run take from the app's own recorder.

## File names

The app saved the audio as WAV; the corpus has it as FLAC in the standard take layout
(`take_partPP-NNN`: run, then file; name order is time order):

| Old | New |
|---|---|
| `audio-001.wav` | `take_part01-001.flac` |
| `audio-002.wav` | `take_part01-002.flac` |
| `audio-003.wav` | `take_part01-003.flac` |
| `audio-004.wav` | `take_part01-004.flac` |
| `audio-005.wav` | `take_part01-005.flac` |
| `audio-006.wav` | `take_part01-006.flac` |
| `audio-007.wav` | `take_part01-007.flac` |
| `audio-008.wav` | `take_part01-008.flac` |
