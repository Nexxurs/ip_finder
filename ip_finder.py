#!/usr/bin/env python3

import socket

IP = "<broadcast>"
PORT = 17155
MESSAGE = "getPI"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.sendto(MESSAGE.encode(), (IP,PORT))
sock.settimeout(1)

try:
	while True:
		data, (ip,port) = sock.recvfrom(1024)
		print("%s: %s" % (data.decode(),ip))
except socket.timeout:
	None
finally:
	sock.close()
input("Press Enter to Close")

