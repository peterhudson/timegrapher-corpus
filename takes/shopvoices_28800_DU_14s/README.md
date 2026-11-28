# Loud voices over a 28,800 bph watch, dial up: 14 s from the end of a shop's Power Reserve Test

Smoke take, contributed with a bug report. It is here to pin a fault: in a Power Reserve Test on Auto, this noise made Auto let the watch's 28,800 lock go and relock at 72,000 bph, and the stop check then read the run at the new rate and ended the test "stopped" while the watch ran on (timegrapher issue #2496, fixed in #2527). Read alone it is not a fault; the recipe below builds the file that shows it. 28,800 bph; lift not known (the shop ran it at the default 52°). No reference figures.

- **Where it came from:** clip C attached to timegrapher #2496 by a user, a watch-service shop's agent. It is take seconds 109,200 to 109,214 of a 30 h Power Reserve Test, cut with `timegrapher excerpt` (1.1.0, 6e94d23). The take was recorded with `record --power-reserve --live` on Windows with a 48 kHz USB microphone. It is the shop owner's own watch, the same take and watch as the two clips mentioned in #2318 (which are not in the corpus). The calibre was not given.
- **Consent:** the comment that attached it says the shop owner releases it under CC0 and that it may go in the public corpus, and that the owner is fine with the voices in it being public.
- **The file:** one file, `take_part01-001.flac`, the attached `clip-C-end-noise.flac` byte for byte (SHA-256 in `corpus.json`): 14.000 s (672,000 frames), 48 kHz, 16-bit mono, with no tags. The audio's MD5 matches the FLAC header's, and the file decodes clean.
- **What is in it** (the reporter's description): loud, high-pitched voices nearby. The watch's beats are under the voices for about the first 7 s; the loudest part covers them from about 7 to 11.5 s, and they are back for the last 2.5 s. Read alone, `analyze` finds no regular beat; with `--bph 28800 --beats`, the beats in both stretches sit on one timing line.
- **Holdout rule:** `scripts/holdout_rule.py` on this file says development (the SHA-256's first byte is 0x95), so it is not holdout.
- **Privacy check:** the file has speech in it by design; the owner agreed to that. It was not listened to by ear at import.
- No `session.toml`, so `regress` does not read this take; tests name it by id.

## The recipe (R16)

This builds `R16.flac`, 772.0 s, from synthetic sound around this clip (`take_part01-001.flac` below). Before the fix, `record --file R16.flac --power-reserve --json` on Auto ended `stopped` with `last_beat_s` 737.89 and `check.to_s` 752.0; the same file with `--bph 28800` ran to 772.0 s and ended `by_hand`. Give each run its own new folder.

```
timegrapher synth w60.wav --duration 60 --bph 28800
python3 -c "import wave; w = wave.open('zeros6.wav', 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(48000); w.writeframes(bytes(2 * 6 * 48000)); w.close()"
timegrapher synth f32.wav --duration 32 --bph 72000
timegrapher synth w640.wav --duration 640 --bph 28800
timegrapher synth w20.wav --duration 20 --bph 28800
timegrapher excerpt w60.wav zeros6.wav f32.wav w640.wav take_part01-001.flac w20.wav --out R16.flac
timegrapher record R16 --position DU --file R16.flac --power-reserve --json
```

The reporter's `R16.flac` had SHA-256 `f35e670c9df7d54ba720df188b38951e61381044259f329664d18c0166c28e4e`, and a rebuild on timegrapher main matched it.
