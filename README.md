# 🛡️ AI Threat Defender

AI Threat Defender is a Python-based cybersecurity project that detects and responds to suspicious files in real time.

## 🚀 Features

- Real-time file monitoring
- Threat detection
- Quarantine system
- Folder scanning
- Live scan progress bar
- Threat history
- GUI dashboard
- Malware hash detection

## 🛠️ Technologies Used

- Python
- PyQt5
- Watchdog
- Psutil
## 📂 Project Structure

AI-Threat-Defender
│
├── 📁 monitor_folder
│   └── Stores files for live monitoring
│
├── 📁 quarantine
│   └── Stores detected suspicious files
│
├── 📁 scanner
│   ├── 📄 __init__.py
│   ├── 📄 file_scanner.py
│   │   └── Handles threat scanning & quarantine
│   │
│   └── 📄 realtime_monitor.py
│       └── Handles real-time file monitoring
│
├── 📄 dashboard.py
│   └── GUI dashboard for the antivirus
│
└── 📄 main.py
    └── Manual file scanning entry point

## ▶️ Run Project

Install dependencies:

pip install watchdog psutil pyqt5

Run dashboard:

python dashboard.py

## ⚠️ Disclaimer

This project is created for educational and defensive cybersecurity purposes only.