#!/usr/bin/python3

import socket
IP = "127.0.0.1"
PORT = 9090
data = b'Hello, world!'
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(data, (IP, PORT))

#DO nc -luc 9090 on the other terminal