# Contributing to Flipper IR Automation

Thank you for your interest in contributing to the Flipper IR Automation project! We welcome contributions from the community to expand our library of supported devices and improve the automation system.

Please take a moment to review this document in order to make the contribution process easy and effective for everyone involved.

## 🤝 How to Contribute

### 1. Reporting Issues
If you encounter a bug, have a feature request, or want to suggest an improvement, please open an issue on GitHub.
- **Bugs**: Describe the issue in detail, including steps to reproduce.
- **Features**: Explain the use case and benefits of the proposed feature.

### 2. Submitting Changes
1.  **Fork the Repository**: Create a fork of the repository to your own GitHub account.
2.  **Create a Branch**: Create a new branch for your changes (e.g., `feature/add-sony-tv`).
3.  **Make Changes**: Implement your changes or add new IR capture files.
4.  **Test Your Changes**: Run the validation script to ensure data integrity.
5.  **Submit a Pull Request**: Open a PR against the `main` branch with a clear description of your changes.

---

## 📡 capturing New IR Signals

We rely on high-quality IR captures to ensure reliable automation. Please follow these guidelines when adding new devices.

### Hardware Requirements
- **Flipper Zero** with the latest firmware (official or Momentum).
- Original remote control for the device.

### Capture Process
1.  Navigate to **Infrared -> Learn New Remote** on your Flipper Zero.
2.  Point the original remote at the Flipper's IR receiver.
3.  Press the button you wish to capture.
4.  **Naming**: Name the signal clearly (e.g., `Power`, `Vol_Up`, `Input_HDMI1`).
5.  **Save**: Save the remote file.

> **Note**: If the protocol is not automatically detected, the Flipper will save the signal in **RAW format**. This is acceptable and often preferred for maximum compatibility.

### File Organization
- Store all `.ir` files in the `data/ir_captures/` directory.
- Use a subdirectory if grouping by room or location (e.g., `data/ir_captures/living_room/`).

### Naming Conventions
Files should follow a consistent naming pattern to avoid conflicts:
`grvroom_<device_type>_<brand>.ir`

Examples:
- `grvroom_tv_samsung.ir`
- `grvroom_ac_daikin.ir`
- `grvroom_fan_dyson.ir`

---

## 🧪 Testing & Validation

Before submitting a PR, please run the validation script to ensure your IR files are correctly formatted.

```bash
python3 tests/validate_ir_data.py
```

This script checks for:
- Valid file extensions (.ir).
- Integrity of RAW data fields (integers only).
- Basic file structure.

---

## 📝 Code Style

- **Documentation**: Update `README.md` or other documentation if your changes affect the user workflow.
- **Python**: Follow PEP 8 guidelines for any Python scripts.
- **Commit Messages**: Use clear, descriptive commit messages (e.g., `Add capture for Sony Bravia TV`).

---

## ⚖️ License

By contributing, you agree that your contributions will be licensed under the MIT License.
