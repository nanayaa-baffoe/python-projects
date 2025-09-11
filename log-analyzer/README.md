# 📝 Log Analyzer

This project is a beginner-friendly **Python log analyzer** that detects suspicious login attempts from system logs.  

---

## 📖 Project Description
- The script reads a `.txt` file containing login attempts.  
- It counts the number of failed login attempts per **user** and **IP address**.  
- If any user/IP has **3 or more failed attempts**, the script flags it as **suspicious**.  

This is a simple demonstration of how **SOC analysts** monitor logs to detect brute-force attacks or compromised accounts.

---

## 🛠️ Skills Practiced
- File handling in Python (`open()`, loops, line parsing)  
- String operations and `split()`  
- Using **dictionaries** to track counts  
- Conditional logic to flag suspicious behavior  

---

## 📂 Example Input (sample log file)
Sep 11 07:32:10 server sshd[1234]: Failed password for alice from 192.168.1.5 port 22 ssh2
Sep 11 07:32:15 server sshd[1235]: Failed password for alice from 192.168.1.5 port 22 ssh2
Sep 11 07:32:20 server sshd[1236]: Failed password for alice from 192.168.1.5 port 22 ssh2
Sep 11 07:33:01 server sshd[1237]: Accepted password for bob from 10.0.0.8 port 22 ssh2


---

## 🖥️ Example Output
192.168.1.5 = suspicious (3 failed attempts)
alice = suspicious (3 failed attempts)


---

## 🚀 How to Run
1. Clone this repo  
   ```bash
   https://github.com/nanayaa-baffoe/python-projects

Navigate into the folder:

cd python-projects/log-analyzer


Run the script:

python log_analyzer.py sample.txt

🔐 SOC Analyst Connection

In real-world SOC operations, log analysis is a critical skill. Analysts often look for:

Multiple failed logins (brute force)

Repeated attempts from the same IP

Unusual login patterns

This project is a mini-simulation of that process using Python.

✅ Next Improvements

Add regex for more precise log parsing

Write suspicious activity to a report file (suspicious_report.txt)

Extend detection to include unusual time-based login patterns


