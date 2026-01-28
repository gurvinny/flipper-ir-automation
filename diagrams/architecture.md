# System Architecture — IR Automation Lab

## Overview

This system enables centralized control of multiple consumer devices using a single Flipper Zero unit by capturing and replaying infrared signals.

---

## Devices Controlled

- Dyson Pure Cool Link
- Emerson AC
- LG TV
- Samsung TV
- Sunset Projection Lamp

---

## Signal Flow

[ Original Remote ] --> [ Flipper IR Capture ] --> [ Signal Storage (.ir) ] --> [ Replay Transmission ] --> [ Target Device ]

---

## Physical Layout

Flipper Zero --> LG TV | Samsung TV | Emerson AC | Dyson Fan | Sunset Lamp

---

## Engineering Notes

- Line-of-sight required for optimal reliability.
- Angle sensitivity observed primarily with sunset lamp.
- No protocol auto-detection → RAW IR used exclusively.
