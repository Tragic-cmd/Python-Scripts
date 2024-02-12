import pyshark
from scapy.all import *

# Define the interface to capture packets from
interface = 'eth0'

# Define the packet filter to capture only specific packets (optional)
filter = 'tcp port 80'

# Define the maximum number of packets to capture (optional)
max_packets = 100

# Capture packets from the specified interface
capture = pyshark.LiveCapture(interface=interface, display_filter=filter, max_packets=max_packets)

# Define a function to analyze each captured packet
def analyze_packet(packet):
    # Print the source and destination IP addresses
    print(f'Source IP: {packet.ip.src}, Destination IP: {packet.ip.dst}')

    # Check if the packet is a TCP packet and print the source and destination ports
    if 'TCP' in packet:
        print(f'Source port: {packet.tcp.srcport}, Destination port: {packet.tcp.dstport}')

    # Check if the packet is an HTTP packet and print the HTTP method and URL
    if 'HTTP' in packet:
        print(f'Method: {packet.http.request_method}, URL: {packet.http.host + packet.http.request_uri}')

    # Print a newline to separate the packets
    print()

# Start capturing packets and call the analyze_packet function for each packet
for packet in capture.sniff_continuously():
    analyze_packet(packet)
