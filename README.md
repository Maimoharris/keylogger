# 🛠️ Python Keylogger Tool

A simple Python-based keylogger using the `pynput` library for educational, red team, and ethical hacking purposes.

---

## ⚠️ Legal Disclaimer

> This tool is provided for **educational purposes only**.  
> Use it **only in environments you own or have explicit written permission to test**.  
> Unauthorized use of this tool may be **illegal** and is strictly prohibited.  
> The author assumes **no responsibility** for any misuse or damage caused by this tool.

---

## 🎯 Features

- Logs all keyboard input system-wide
- Detects and logs special keys (e.g., Enter, Tab, Space, Backspace, Escape)
- Saves logs to a file named `log.txt`
- Colorful ASCII banner for terminal display
- Lightweight and runs in the background until Esc is pressed

---

## 🧰 Requirements

- Python 3.x
- `pynput` library

Install the required dependency:

```bash
pip install pynput

🚀 Installation

    Clone the repository:

git clone https://github.com/Maimoharris/keylogger.git
cd keylogger

Run the script as root:

    sudo python3 keylogger.py

    ❗ Running as root ensures full system-wide keyboard access.

▶️ Usage

Once executed, the tool will:

    Display a colorful terminal banner.

    Begin listening for keystrokes in the background.

    Continue logging until the Esc key is pressed.

    Save all logged input to log.txt in the current directory.


Special keys are wrapped in brackets, e.g.:

    [Tab]

    [Enter]

    [Shift]

    [Backspace]

🔧 Customization Ideas

You can extend this tool by:

    Adding timestamps to each key press.

    Encrypting the log file for security.

    Sending logs via email or to a secure remote server.

    Running it silently without a console window (Windows/GUI setups).

📞 Contact

Author: MAIMO HARRIS
Phone: +237 680 226 898
🧠 Final Note

Always stay ethical and legal in your cybersecurity journey.
Respect privacy. Use your skills to protect, not exploit.
Happy hacking!


Let me know if you’d like this in a downloadable file or want to turn it into a GitHub project with proper license and structure.

