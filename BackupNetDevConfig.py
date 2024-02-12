import paramiko
import time

# Set up SSH connection parameters
hostname = '192.168.1.1'
username = 'username'
password = 'password'
port = 22

# Set up the commands to be executed on the device
commands = ['enable', 'password', 'terminal length 0', 'show running-config']

# Set up the filename for the backup file
filename = 'backup.cfg'

# Set up the SSH client and connect to the device
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, port=port, username=username, password=password)

# Send the commands to the device and wait for the output
output = ''
for command in commands:
    stdin, stdout, stderr = client.exec_command(command)
    output += stdout.read().decode()

# Save the output to a file
with open(filename, 'w') as f:
    f.write(output)

# Disconnect from the device
client.close()
