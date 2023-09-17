#!/usr/bin/python3
import socket

IP = "0.0.0.0"
PORT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((IP, PORT))

while True:
    data, (ip, port) = socket.recvfrom(1024)
    print("Sender : {} and Port : {}".format(ip, port))
    print("Received message: {}".format(data))

# nc -u 10.02.7 9090
#udp_server.py