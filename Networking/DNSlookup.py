# The script allows the user to input the number of hostnames they want to lookup, and then prompts them to enter each hostname one at a time. It then iterates through the list of hostnames and performs a DNS lookup for each one.
# I've also added error handling for cases where a hostname cannot be resolved. If the socket.gethostbyname or socket.gethostbyaddr functions raise a socket.gaierror exception, the script will print an error message indicating that the hostname could not be resolved, along with the exception message.
import socket

def dns_lookup(host):
    try:
        ip = socket.gethostbyname(host)
        hostname = socket.gethostbyaddr(ip)[0]
        print(f'{host} - Hostname: {hostname} IP Address: {ip}')
    except socket.gaierror as e:
        print(f'Error: Could not resolve {host} - {e}')

if __name__ == '__main__':
    num_hosts = int(input('Enter the number of hostnames to lookup: '))
    hosts = []
    for i in range(num_hosts):
        host = input(f'Enter hostname #{i+1}: ')
        hosts.append(host)
    
    for host in hosts:
        dns_lookup(host)

# UNFINISHED
