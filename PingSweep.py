# This script will iterate through the range of IP addresses specified by start_ip and end_ip, and for each IP address, it will send a ping request with a timeout of 1 second using the ping3.ping() function. 
# If a response is received within the timeout period, the script will print a message indicating that the device at that IP address is online.

import ping3

# Set up the IP address range to scan
ip_range = '192.168.1.'
start_ip = 1
end_ip = 254

# Ping each IP address in the range and print the results
for i in range(start_ip, end_ip + 1):
    ip = ip_range + str(i)
    response = ping3.ping(ip, timeout=1)
    if response is not None:
        print(f'{ip} is online')
