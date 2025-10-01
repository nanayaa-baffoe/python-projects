
# Simple Log File Analyzer
# Author: Enochlin Baffoe
# This script reads a log file and reports suspicious activity based on failed login attempts.



from operator import itemgetter
fname = input('Enter log filename : ')
fhandle = open(fname)

display = int(input('Enter how many top IPs to display: '))
threshold = int(input('Enter suspicious threshold: '))
ip_address = {}
for line in fhandle:
    line = line.strip()
    if line:
        address=  line.split()[0]
        ip_address[address] = ip_address.get(address , 0)+1
new_list = list(ip_address.items())
new_list.sort(key= itemgetter(1) , reverse=True)

top_display = new_list[0:display]

result = []
for key , value in top_display:
    if value >= threshold:
        label = 'suspicious'
    else:
        label = 'normal'
    output = f'{key}: {value}: {label}' 
    print(output)
    result.append(output)
        
    

with open('report.txt', 'w') as file:
    file.write('\n'.join(result))

print('successfully uploaded')
