from scapy.all import *

print("SENDING SPOOFED ICMP PACKET.........")
ip = IP(src="1.2.3.4", dst="93.184.216.34") #IP Layer
udp = UDP(sport=8888, dport=9090) #UDP Layer
data = "Hello UDP!\n" #Payload

#Spoofing ICMP packet
icmp = ICMP()
pkt = ip/icmp
pkt.show()
send(pkt,verbose=0)

#Spoofing UDP packet
pkt = ip/udp/data
pkt.show()
send(pkt,verbose=0)