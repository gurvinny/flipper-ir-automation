# Technical Findings & Engineering Notes

This document records the observations and lessons learned during the development and testing of the IR Automation System.

---

## 📡 Capture Behavior & Protocols

### Observations
- **Method**: All remotes were captured using the standard Flipper Zero IR learning mode.
- **Protocol Detection**: Most devices did not trigger an automatic protocol match (e.g., NEC, RC5).
- **Format**: Consequently, signals were stored in **RAW format** (timing of pulses and gaps).
- **Consistency**: Capture quality was consistent across brands, with minimal noise in the recorded signal.

### Implication
RAW capture files are significantly larger than decoded protocol files but offer **universal compatibility** since they replay the exact physical signal without needing to understand the underlying data structure.

---

## ⚡ Replay Performance

### Reliability Metrics
| Metric | Result | Notes |
| :--- | :--- | :--- |
| **Effective Range** | 1.5 – 2.0 meters (5–6 ft) | Consistent with standard IR remote power. |
| **Transmission Rate** | 100% Success | No dropped commands observed during testing. |
| **Latency** | < 100ms | Indistinguishable from original remotes. |

### Angle Sensitivity
- **High Sensitivity**: The **Sunset Projection Lamp** requires precise alignment (approx. ±15° from center).
- **Low Sensitivity**: The **LG TV** and **Emerson AC** receivers have a wide acceptance angle (approx. ±60°), allowing control from off-axis positions.

---

## 🗄️ Data Organization Strategy

We adopted a location-based directory structure rather than a brand-based one.

### Structure
```
data/ir_captures/
└── grv_room/
    ├── grvroom_tv_lg.ir
    ├── grvroom_ac_emerson.ir
    └── ...
```

### Justification
1.  **Logical Grouping**: Devices are often controlled in clusters (e.g., "Turn off everything in the living room").
2.  **Portability**: The entire `grv_room` folder can be copied to a new Flipper Zero to instantly provision control for that specific physical space.
3.  **Deployment**: Simplifies the user interface on the Flipper Zero, keeping relevant remotes together.

---

## 🎓 Lessons Learned

### 1. Naming Conventions are Critical
Early tests resulted in confusion between similar remotes (e.g., "TV Remote" vs. "Bedroom TV"). adopting the `grvroom_<device>_<brand>` schema solved this by providing unique, descriptive, and sortable filenames.

### 2. RAW vs. Decoded
While decoded signals are cleaner and editable, **RAW captures are safer** for initial reverse engineering. They remove the risk of incorrect protocol decoding which can lead to non-functional buttons.

### 3. Backup & Versioning
Exporting files from the SD card to a Git repository is essential. It prevents data loss if the physical SD card is corrupted and allows for tracking changes to signal sets over time.
