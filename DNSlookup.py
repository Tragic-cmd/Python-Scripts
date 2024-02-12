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
