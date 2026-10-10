# Empty stand (silence), 2026-10-10, rear USB root port, AGC off
- silence_mic10.flac: 300 s at Mic 10/16 from 17:40:58.5Z. silence_mic8.flac: 300 s at Mic 8/16 from 17:45:58.9Z. The room was normal (no AC at the time, keyboard idle).

| | Mic 10/16 | Mic 8/16 |
|---|---|---|
| RMS (full band) | −42.2 dBFS | −45.5 dBFS |
| Power above 1.5 kHz | −43.0 | −46.3 |
| …minus the 1 kHz comb (±5 Hz around k·1 kHz) | **−47.8** | **−51.2** |
| Comb lines alone | −44.7 | −48.0 |

- **The noise above 1.5 kHz is dominated by a comb of exact 1 kHz harmonics** (3, 4, 5, 6, **7 (strongest, −49.8 dBFS)**, 9, 10 kHz…). That's USB start-of-frame (1 ms) interference from the host. Notching it would lower the noise floor in the tick band by about **4.8 dB**.
- **The 7 kHz line measures 7000.140 Hz on the card clock**, which is a true 7000 Hz with the card 20.0 ppm slow. That agrees with the −20 to −22 ppm from the clock logs. **The comb is a built-in card-clock reference:** the engine can calibrate the sound-card rate from any recording, with no NTP needed.
- These are the same 5/6/7 kHz lines seen on day 1 through the ASMedia hub, so they come from the device or USB itself, not the hub.
