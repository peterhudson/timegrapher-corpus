# USB lines from a hub's clock: an Explorer II replica, dial up, with the mic behind a Thunderbolt drive

Smoke take, contributed with a bug report. It is here to pin a fault: the mic was plugged into a Thunderbolt drive's USB port, and that drive's own USB controller makes the 1 ms frames, so the USB lines read the sound card about 151 ppm fast against the drive's crystal instead of the computer's (timegrapher issues #2291 and #2283). A rate corrected by those lines is about 13 s/d wrong. 28,800 bph; lift 59° as the reporter set it. No reference figures.

- **Where it came from:** the excerpt in the report bundle attached to timegrapher #2291 (`timegrapher-report-20261125T201552Z.zip`, made 2026-11-25 20:15:56Z with the desktop app 1.1.0, 6e94d23, on macOS). The bundle's consent says `corpus_cc0: true`, `audio_included: true` and `listened_back: true`. It is the reporter's own watch, not the one in the `dd3285_explorer2_*` takes.
- **The watch:** an Explorer II replica with a Dandong 3285, dial up, fully wound (the reporter's note). Recorded with a "USB PnP Sound Device" pickup.
- **The file:** one file, `take_part01-001.flac`, the bundle's `audio/excerpt.flac` byte for byte (SHA-256 in `corpus.json`): 95.595 s (4,588,544 frames) from the start of the take, 48 kHz, 16-bit mono, with no tags. The take itself was recorded at 24-bit; the report's excerpt is 16-bit. The audio's MD5 matches the FLAC header's.
- **What was found in it** (#2283): six USB start-of-frame lines agreeing to 0.05 ppm, reading the card at +151.1 ppm. The same mic plugged straight into the computer read +9.3 ppm (#2292, whose audio is not in the corpus).
- **Holdout rule:** `scripts/holdout_rule.py` on this file says development (the SHA-256's first byte is 0xdc), so it is not holdout.
- **Privacy check:** a spectrogram of the whole file shows the ticks, steady tones and the USB lines, with no bursts like speech. It was not listened to by ear at import; the reporter listened back before sending.
- No `session.toml`, so `regress` does not read this take; tests name it by id.
