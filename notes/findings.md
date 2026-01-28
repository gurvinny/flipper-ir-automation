# Technical Findings & Engineering Notes

## Capture Behavior

- All remotes captured using Flipper IR learning mode.
- No protocol automatically detected.
- Signals stored in RAW format.
- Capture quality was consistent across all remotes.

---

## Replay Performance

- Reliable operation at 5–6 feet.
- No failed transmissions.
- Minimal latency.
- Best reliability achieved with direct line-of-sight.

---

## Angle Sensitivity

- Sunset lamp required more precise alignment.
- TVs and AC exhibited broad acceptance angles.

---

## Storage Strategy

Signals grouped by physical environment:

grv_room/

This allows:

- Logical grouping
- Easy portability
- Rapid deployment

---

## Lessons Learned

- File naming conventions are critical at scale.
- RAW capture ensures maximum compatibility.
- SD export allows long-term project documentation and version control.
