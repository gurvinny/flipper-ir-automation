# Flipper IR Automation System — Signal Capture, Analysis & Room Control

## Objective
Design and implement a unified infrared (IR) automation system using Flipper Zero by reverse engineering consumer remote signals, capturing and organizing IR codes, and reliably replaying them to control multiple devices within a single environment.

This project focuses on:
- Signal capture and protocol analysis
- Device interoperability
- Structured data organization
- Repeatable automation workflows
- Security-conscious experimentation

---

## Devices Controlled (Authorized Environment)

All devices used in this project are personally owned and located within my room.

- Dyson Pure Cool Link (fan + air purifier)
- Emerson Air Conditioner
- LG Television
- Samsung Television
- Sunset Projection Lamp

---

## Hardware & Tools

- Flipper Zero (running Momentum firmware)
- Stock IR transmitter and receiver
- Original manufacturer remotes
- MicroSD card (for signal export & versioning)
- qFlipper (file transfer & backup)

---

## Methodology

### 1. Signal Capture
IR signals were captured using:

Infrared → Learn New Remote

Each button on the original remote was pressed individually and labeled in real time.
No protocol was automatically detected, so all signals were stored and replayed using RAW capture format.

---

### 2. Signal Labeling & Organization

All captured remotes were saved under a structured namespace:
grv_room/

Each device was assigned a unique file with standardized naming.

---

### 3. Signal Export & Version Control

All `.ir` files were exported from the Flipper Zero SD card and versioned into this repository for:

- Reproducibility
- Documentation
- Backup
- Engineering analysis

---

### 4. Testing & Validation

Each signal was replayed multiple times at varying distances and angles to validate:

- Reliability
- Range
- Accuracy
- Device responsiveness

---

## Performance & Reliability

| Metric | Observation |
|----------|--------------|
| Effective Range | 5–6 feet (device dependent) |
| Accuracy | 100% successful replay |
| Angle Sensitivity | Minor on sunset lamp |
| Latency | Instantaneous |
| Replay Failures | None |

---

## Architecture & System Flow

High-level control flow:

Flipper Zero
│
IR Signal Transmission
│
Target Devices (TVs, AC, Fan, Lamp)

(See `/diagrams/architecture.md` for detailed system flow.)

---

## Security & Engineering Focus

This project emphasizes:

- Controlled signal capture
- Protocol awareness
- Data integrity
- Ethical research boundaries
- Hardware-security experimentation mindset

No unauthorized devices or environments were accessed.

---

## Challenges & Lessons Learned

- RAW IR capture is highly reliable but increases file size.
- Some consumer devices require precise angles for optimal signal reception.
- Signal naming discipline is critical for long-term scalability.

---

## Future Enhancements

- Macro-based automation modes (Movie Mode, Sleep Mode)
- MQTT / Home Assistant integration
- RF + IR hybrid automation workflows
- Protocol-level decoding and classification

---

## Ethics & Authorization

All experiments were conducted exclusively on hardware I own or environments where I have explicit authorization.

This repository is intended strictly for educational, research, and engineering demonstration purposes.
