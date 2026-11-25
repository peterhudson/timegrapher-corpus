# Silent start: 10 s of digital zeros, the empty stand, then the Yacht-Master 42 replica, played through a fake mic

Smoke take, built from other corpus takes. It is here to pin a fault: a take that opens on exact digital zeros, read with the beat rate given, found no step from the stand's noise onto the watch, so the stand's lead was read in (timegrapher issue #2189, fixed by #2190). Most microphones never give exact zeros; a gated USB microphone or a virtual input can. This one came from a virtual input. 28,800 bph; lift 55° for the watch's part, as in `ym42_DU_2h`. No reference figures.

- **How it was made:** recorded on 2026-11-21 with the desktop app's Quick Listen at Average Over 10 s, during a walkthrough of timegrapher #2187 (head 138b546), on Linux with corpus audio played into a fake PulseAudio microphone. Listening started about 10 s before the sound did. One file, `take_part01-001.flac`: 249.344 s (11,968,512 frames), 48 kHz, 16-bit mono, as the app saved it, with no tags. The audio's MD5 matches the FLAC header's.
- **What is in it** (seconds of this take; every stretch was checked sample by sample against the source file):

| From (s) | To (s) | Sound | Source |
|---:|---:|---|---|
| 0 | 10.107 | exact zeros | none (the fake mic before the sound came) |
| 10.107 | 80.070 | the empty stand | `silence_empty_stand` file `take_part01-001`, 0.037 s to 70 s |
| 80.070 | 180.070 | the watch, dial up | `ym42_DU_2h` file `take_part01-001`, 0 s to 100 s; 2 samples differ by 1 (at 109.32 s and 109.57 s) |
| 180.070 | 240.070 | the empty stand | `silence_empty_stand` file `take_part01-001`, 100 s to 160 s |
| 240.070 | 249.344 | exact zeros | none |

- From 10.070 s to 10.107 s the source's first 0.037 s came through as zeros, so the zeros run to 10.107 s.
- Every source is a corpus take under CC0, so this take is too. It holds no speech or room sound beyond what those takes hold.
