sudo ip addr add 192.168.60.6/24 enp0s3
dig www.example.com
List IP address on Network Interface
ip -br address
ip addr
ip route
nc <ip> <port> sends out TCP
nc -u <ip> <port> sends out UDP
tcpdump -n -i eth0
-n: do not resolve the IP address to host name
-i: sniffing on this interface
tcpdump -n -i eth0 -vvv “tcp port 179”
-vvv: asks the program to produce more verbose output.
tcpdump -i eth0 -w /tmp/packets.pcap
saves the captured packets to a PCAP file
use Wireshark to display them


Find out interface name:
ifconfig

tO enable/disable IP forwarding:
sysctl net.ipv4.ip_forward=1
sysctl net.ipv4.ip_forward=0