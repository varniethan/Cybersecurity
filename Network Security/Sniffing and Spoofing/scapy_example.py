#!/usr/bin/python3
from scapy.all import *
pkt = sniff(iface='enp0s3', filter='icp or udp', count=10)
pkt.summary()

def process_packet(pkt):
    #hexdump(pkt)
    pkt.show()
    print("---------------")

f = 'idp and dst portrange 50-55 or icmp'

sniff(iface='enp0s3', filter=f, prn=process_packet)

# pkt = Ether()/IP()/UDP()/"hello"
# pkt
# pkt.payload
# pkt.payload.payload
# pkt.payload.payload.payload
# pkt.getlayer(UDP)
# pkt.getlayer(RAW)
# pkt[Raw]
# pkt.haslayer(Raw)

