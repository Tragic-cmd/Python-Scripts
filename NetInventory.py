import nmap
import netdisco

def get_device_inventory():
    # Initialize Nmap scanner
    nm = nmap.PortScanner()

    # Scan network for live hosts
    nm.scan(hosts='192.168.1.0/24', arguments='-sn')

    # Get list of live hosts
    live_hosts = nm.all_hosts()

    # Initialize Netdisco discovery
    nd = netdisco.Discovery()

    # Loop through live hosts and get device information
    devices = []
    for host in live_hosts:
        # Try to get device information using Netdisco
        try:
            device_info = nd.get_info(host)

            # Add device information to list of devices
            devices.append({
                'ip_address': host,
                'mac_address': device_info['mac'],
                'operating_system': device_info['manufacturer']
            })

        # Handle errors when device information cannot be obtained
        except Exception as e:
            print(f"Error: {e}. Skipping host {host}.")

    # Print list of devices with formatted output
    print("\nDevice Inventory:\n")
    print("{:<20} {:<20} {:<20}".format('IP Address', 'MAC Address', 'Operating System'))
    for device in devices:
        print("{:<20} {:<20} {:<20}".format(device['ip_address'], device['mac_address'], device['operating_system']))

# Call function to get device inventory
get_device_inventory()
