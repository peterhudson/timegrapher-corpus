# Omega 3861 (co-axial escapement), dial up, 10.6 min, with a Witschi reading

Smoke take, contributed by an anonymous user: the same contributor as
`omega3861_coaxial_DU_10min`. It is the corpus's first co-axial take with a
reading from a commercial timegrapher in co-axial mode close to it in time,
so the co-axial estimate (beta) can be set against an outside instrument.
It is not tier **paired**: the two readings were not taken at the same
time, and tg has not read the file.

- **Where it came from:** the contributor's own take, recorded with the
  desktop app (timegrapher-app 1.1.0) on a commercial timegrapher's pickup,
  Quick Listen, 21,600 bph, lift 36°, dial up, from 2026-11-26 22:56:56Z to
  23:07:32Z. The contributor agreed to the recordings being published
  (timegrapher #2313). The pickup's name was removed from
  `raw/app_session.json`; nothing else in the app's files was changed.
- **Same watch as `omega3861_coaxial_DU_10min`:** assumed, not stated by the
  contributor. The engine's unlock-to-drop intervals agree: 6.69 ms and
  6.00 ms here, 6.72 ms and 6.00 ms there.
- **The file:** one file, `take_part01-001.flac`, the app's
  `audio-001.flac` byte for byte (`raw/file_map.txt`; SHA-256 in
  `corpus.json`): 635.584 s (30,508,032 frames, which is also the last frame
  count in `clock.csv`), 48 kHz, 16-bit mono, with no tags. It decodes
  without error.
- `raw/app_session.json` and `raw/app_session.toml.txt` are the app's own
  session files (the toml renamed so `regress` does not read `raw/` as a
  session). `clock.csv` is the app's clock log. The app logged one note,
  "paused", at the end. The app's `result` block is its last live reading
  in 1.1.0, before co-axial support; it is not a checked reading.
- **Lift angle:** 36° on both instruments, the contributor's setting. No
  checked source gives one for the 3861, so `session.toml` says
  `lift_known = false`. Any amplitude read from this take is a co-axial
  estimate (beta).
- **Holdout rule:** `scripts/holdout_rule.py` on this file says development
  (the SHA-256's first byte is 0xd0), so it is not holdout.
- **Privacy check:** a spectrogram of the whole file shows the ticks and
  steady tones, with no bursts like speech. It was not listened to by ear
  at import.

## The reference reading

Read from the contributor's photograph of the instrument's screen. The
photograph itself is not published. Its timestamp is 2026-11-26 23:09:42Z,
about 2 minutes after the take ended, so the watch had been off this
pickup and onto the other instrument; wind state and position may differ.

| Instrument | Setting | Rate | Beat error | Amplitude |
|---|---|---|---|---|
| Witschi Chronoscope | Mode Co-Axial, 21,600 A/h, lift 36.0°, integration time 2 s | +0.68 s/d | 0.07 ms | 292.3° |

The contributor also sent a screenshot of the desktop app (1.1.0, Quick
Listen, Auto 21600, lift 36°, dial up) 5 min 37 s into a listen that
started earlier the same evening. That listen is **not** this file. It read
−1.0 ± 4.7 s/d, 301° ± 3° and 0.48 ± 0.31 ms. Version 1.1.0 had no
co-axial reading, so that beat error is the drop's, which means little on
a co-axial.

## What timegrapher reads

`timegrapher analyze take_part01-001.flac --calibre "Omega 3861" --lift 36`
at main f153a26 (2026-11-27), whole take, clock from the 8 USB lines in
the recording:

| Reading | Rate | Beat error (unlock) | Amplitude (co-axial estimate, beta) |
|---|---|---|---|
| Whole take | −2.2 s/d | 0.10 ms | 307° (sides 289° and 325°) |
| Last minute (575 s to end) | −2.0 s/d | 0.10 ms | 304° (sides 291° and 323°) |

Against the Witschi: beat error agrees within 0.03 ms. Rate is 2.9 s/d
slower, inside the spread of this watch's 10 s rates (5th to 95th
percentile −4.6 to +10.2 s/d, with a swing that repeats every 59 s), which
a 2 s reading cannot average out. Amplitude is 12° to 15° (about 5%)
higher; the Witschi's figure sits near timegrapher's lower side.
