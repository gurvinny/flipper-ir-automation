# 🛡️ Security Policy & Vulnerability Disclosure

This project is committed to maintaining the integrity of IR signal intelligence and ensuring a secure environment for automation research. We welcome contributions from the security research community and value responsible disclosure.

## 📊 Supported Versions

Security updates and patches are prioritized for the following branches:

| Branch | Status | Security Support |
| :--- | :--- | :--- |
| `main` | ![Active](https://img.shields.io/badge/Status-Active-brightgreen) | Full Support |
| `stable` | ![Maintenance](https://img.shields.io/badge/Status-Maintenance-yellow) | Critical Fixes Only |

## 🔍 Vulnerability Scope

We are particularly interested in the following security-relevant issues:

*   **Signal Integrity**: Vulnerabilities that could lead to unauthorized modification of captured `.ir` data.
*   **Validation Bypass**: Methods to circumvent the `validate_ir_data.py` checks with malicious payloads.
*   **Remote Execution/DoS**: Flaws in automated replay scripts or data parsing that could lead to system instability.

### 🚫 Out-of-Scope Research
*   Physical access attacks on the Flipper Zero hardware.
*   Social engineering attacks against repository contributors.
*   Vulnerabilities in third-party firmware (e.g., Momentum) unless triggered specifically by our signal data.

## 🛡️ Safe Harbor / Ethical Research Guidelines

To encourage security research and protect researchers, we promise not to pursue legal action against individuals who:

1.  **Test only on authorized hardware**: Ensure you own or have permission to test the target IR devices.
2.  **Avoid disruption**: Do not perform research that impacts the availability or safety of others' environments.
3.  **Practice Responsible Disclosure**: Provide us a reasonable timeframe to address findings before public release.
4.  **Adhere to laws**: Comply with all applicable local, state, and federal laws.

## 📨 Reporting a Vulnerability

If you identify a security vulnerability, please **do not open a public issue**. Instead, follow the coordinated disclosure process:

1.  **GitHub Security Advisory**: Navigate to the [Security](https://github.com/gurvinny/flipper-ir-automation/security) tab and select "Report a vulnerability" to open a private draft.
2.  **Required Information**:
    *   Detailed description of the vulnerability.
    *   Steps to reproduce (Proof of Concept).
    *   Potential impact assessment.
    *   Suggested remediation (if available).

## ⏱️ Response & Disclosure Process

*   **Acknowledgment**: Within 48 hours of report receipt.
*   **Verification**: Initial assessment and confirmation within 7 business days.
*   **Remediation**: Time-to-fix varies by severity, but we aim for 30–90 days for full resolution.
*   **Public Disclosure**: Conducted via GitHub Security Advisories once a patch is available and verified.

---
*Thank you for helping keep our signal intelligence secure.*
