import subprocess
import sys

# List of commands to disable sleep settings
commands = [
    'powercfg -change -standby-timeout-ac 0',
    'powercfg -change -standby-timeout-dc 0',
    'powercfg -change -hibernate-timeout-ac 0',
    'powercfg -change -hibernate-timeout-dc 0',
    'powercfg -change -monitor-timeout-ac 0',
    'powercfg -change -monitor-timeout-dc 0',
]

# Check if the script is running as an administrator
if not sys.argv[-1] == 'asadmin':
    print("Please run the script as an administrator")
    sys.exit(0)

# Disable sleep settings using the list of commands
for cmd in commands:
    output = subprocess.check_output(cmd, shell=True)
    print(output.decode())

# Set power plan to High Performance
cmd = 'powercfg -setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c'
output = subprocess.check_output(cmd, shell=True)
print(output.decode())
