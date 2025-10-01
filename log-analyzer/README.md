
📝 Log Analyzer

This project is a beginner-friendly Python log analyzer that detects suspicious login attempts from system logs.

📖 Project Description

Reads a .txt file containing login attempts

Counts the number of attempts per IP address

Flags an IP as suspicious if its request count is above a defined threshold

This is a simple demonstration of how SOC analysts monitor logs to detect brute-force attacks or compromised accounts.

🛠️ Skills Practiced

File handling in Python (open(), loops, line parsing)

String operations and split()

Dictionaries for event counting

Conditional logic to flag suspicious behavior

📂 Example Input (sample log file)
192.168.1.10 - - [01/Oct/2025:08:45:10] "GET /index.html"
10.0.0.5 - - [01/Oct/2025:08:45:12] "POST /login"
192.168.1.10 - - [01/Oct/2025:08:45:14] "POST /login"
203.0.113.55 - - [01/Oct/2025:08:45:16] "GET /admin"
192.168.1.10 - - [01/Oct/2025:08:45:20] "POST /login"

🖥️ Example Output
192.168.1.10: 3: suspicious
10.0.0.5: 1: normal
203.0.113.55: 1: normal

🚀 How to Run

Clone this repo

git clone https://github.com/nanayaa-baffoe/python-projects


Navigate into the folder

cd python-projects/log-analyzer


Run the script

python log_analyzer.py sample.txt

🔐 SOC Analyst Connection

In real-world SOC operations, log analysis is a critical skill. Analysts often look for:

Multiple failed logins (brute-force attempts)

Repeated requests from the same IP

Unusual or abnormal access patterns

This project is a mini-simulation of that process using Python.

✅ Next Improvements

 Add regex for more precise log parsing

 Write suspicious activity to a report file (report.txt)

 Extend detection to include time-based anomalies in login attempts
