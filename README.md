🔐 Python Security Log Analyzer

A beginner-friendly cybersecurity project built with Python to analyze authentication logs and identify repeated failed login attempts.

📌 Features
Reads authentication events from a log file.
Counts successful and failed login events.
Groups failed attempts by IP address.
Generates alerts when an IP reaches the configured failure threshold.
Handles a missing log file with an error message.
🛠️ Technologies
Python 3
collections.Counter
pathlib
📂 Project Structure
python-security-log-analyzer/
├── analyzer.py
├── sample_logs.txt
└── README.md

▶️ How to Run
Install Python 3.
Download or clone this repository.
Open a terminal in the project folder.
Run:
python3 analyzer.py

⚙️ Configuration

The default alert threshold is 3 failed login attempts per IP address.

Change the THRESHOLD value in analyzer.py to adjust it.

📊 Example Output
=== Security Log Analysis ===
Total login events: 8
Successful logins: 3
Failed login events: 5

=== Failed Attempts by IP ===
203.0.113.25: 3 failed attempts
  ALERT: Repeated failures detected for 203.0.113.25
198.51.100.42: 2 failed attempts

🎯 Project Goal

This project demonstrates foundational Python programming, log parsing, data aggregation, and basic security event detection.

⚠️ Limitations

This is an educational demonstration using sample logs. It counts failed attempts across the entire file and does not yet correlate events by time window or validate IP addresses.

👨‍💻 Author

Afnan912

GitHub Profile
