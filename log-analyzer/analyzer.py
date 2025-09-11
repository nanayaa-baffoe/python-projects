
# Simple Log File Analyzer
# Author: Enochlin Baffoe
# This script reads a log file and reports suspicious activity based on failed login attempts.





fname = input("Please enter the file name: ")
fhandle = open(fname)

# Dictionaries to track failures
user_failures = {}
ip_failures = {}

for line in fhandle:
    words = line.split()

    if "FAIL" in words:  #Check if this was a failed login
        user = words[7]  # extract username
        ip = words[9]    # extract IP address

        # Count user failures
        user_failures[user] = user_failures.get(user, 0) + 1

        # Count IP failures
        ip_failures[ip] = ip_failures.get(ip, 0) + 1

# Suspicious users
print("\nSuspicious Users:")
for user, count in user_failures.items():
    if count >= 3:
        print(f"{user} = suspicious ({count} failed attempts)")

# Suspicious IPs
print("\nSuspicious IPs:")
for ip, count in ip_failures.items():
    if count >= 3:
        print(f"{ip} = suspicious ({count} failed attempts)")
