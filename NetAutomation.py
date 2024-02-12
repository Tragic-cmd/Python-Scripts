import netmiko
import logging

# Define the devices to be configured
devices = [
    {
        'device_type': 'cisco_ios',
        'ip': '192.168.0.1',
        'username': 'admin',
        'password': 'password',
    },
    {
        'device_type': 'cisco_ios',
        'ip': '192.168.0.2',
        'username': 'admin',
        'password': 'password',
    },
]

# Define the configuration commands to be sent to the devices
config_commands = [
    'interface GigabitEthernet0/0',
    'ip address 192.168.0.3 255.255.255.0',
    'no shutdown',
]

# Set up logging
logging.basicConfig(filename='network_config.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

# Loop through each device and configure it
for device in devices:
    try:
        # Connect to the device
        net_connect = netmiko.ConnectHandler(**device)

        # Send the configuration commands
        output = net_connect.send_config_set(config_commands)

        # Print the output of the configuration commands
        print(f"Configuration applied to {device['ip']}:\n{output}")

        # Log the output of the configuration commands
        logging.info(f"Configuration applied to {device['ip']}:\n{output}")

    except Exception as e:
        # Print and log any errors that occur
        print(f"Error configuring {device['ip']}: {str(e)}")
        logging.error(f"Error configuring {device['ip']}: {str(e)}")

    finally:
        # Disconnect from the device
        net_connect.disconnect()
