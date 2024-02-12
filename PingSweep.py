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
