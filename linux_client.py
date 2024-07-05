#!/usr/bin/env python3

# Hostname:

import socket

HOST = "127.0.0.1"
PORT = 58761

name = input("Who are you : ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF - Address Family
# INET - Internet

client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_socket.connect((HOST, PORT))
if client_socket == PORT:
	print(client_socket.recv(2048).decode())
while True:
	msg = input("Message: ")
	if msg == "quit":
		break
	msg = name + ": " + msg
	socket.sendall(msg.encode())
socket.close()
