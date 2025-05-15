from scapy.all import *
from scapy.layers.inet import IP, TCP

# Windows compatibility fix
conf.use_pcap = True
conf.L3socket = conf.L3socket

def packet_callback(packet):
    if packet.haslayer(IP):
        src = packet[IP].src
        dst = packet[IP].dst
        proto = packet[IP].proto
        print(f"[+] {src} -> {dst} | Protocol: {proto}")

print("Sniffing traffic (Ctrl+C to stop)...")
sniff(prn=packet_callback, store=0, iface=conf.ifaces.dev_from_index(1))