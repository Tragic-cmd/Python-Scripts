import argparse
import socket
import threading
import time

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f'Port {port} is open on {ip}')
        sock.close()
    except:
        pass

def scan_ip(ip, start_port, end_port):
    print(f'Scanning {ip}...')
    for port in range(start_port, end_port + 1):
        scan_port(ip, port)

def main():
    parser = argparse.ArgumentParser(description='Scan a range of IP addresses for open ports.')
    parser.add_argument('start_ip', type=int, help='the starting IP address')
    parser.add_argument('end_ip', type=int, help='the ending IP address')
    parser.add_argument('start_port', type=int, help='the starting port number')
    parser.add_argument('end_port', type=int, help='the ending port number')
    args = parser.parse_args()

    threads = []
    for i in range(args.start_ip, args.end_ip + 1):
        ip = f'192.168.1.{i}'
        t = threading.Thread(target=scan_ip, args=(ip, args.start_port, args.end_port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == '__main__':
    start_time = time.time()
    main()
    print(f'Time elapsed: {time.time() - start_time:.2f} seconds')
