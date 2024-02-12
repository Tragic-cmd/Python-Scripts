import nmap

# Set up the IP address range to scan
ip_range = '192.168.1.1/24'

# Set up the nmap scanner and run the scan
nm = nmap.PortScanner()
nm.scan(hosts=ip_range, arguments='-sP')

# Print the details of each device found on the network
for host in nm.all_hosts():
    print('----------------------------------------------------')
    print(f'Host : {host} ({nm[host].hostname()})')
    print(f'State : {nm[host].state()}')
    if 'mac' in nm[host]['addresses']:
        print(f'MAC Address : {nm[host]["addresses"]["mac"]}')
    if 'vendor' in nm[host]['addresses']:
        print(f'Vendor : {nm[host]["addresses"]["vendor"]}')
    for proto in nm[host].all_protocols():
        lport = nm[host][proto].keys()
        for port in sorted(lport):
            print(f'Port : {port}\tState : {nm[host][proto][port]["state"]}')
            if 'name' in nm[host][proto][port]:
                print(f'Name : {nm[host][proto][port]["name"]}')
            if 'product' in nm[host][proto][port]:
                print(f'Product : {nm[host][proto][port]["product"]}')
            if 'version' in nm[host][proto][port]:
                print(f'Version : {nm[host][proto][port]["version"]}')
            if 'extrainfo' in nm[host][proto][port]:
                print(f'Extra Info : {nm[host][proto][port]["extrainfo"]}')
