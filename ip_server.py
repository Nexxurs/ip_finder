import socket

UDP_PORT = 17155
UDP_IP = ''

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(None)
try:
	while True:
		data, addr = sock.recvfrom(1024)
		txt = data.decode()
		if txt == "getPI":
			host = socket.gethostname()
			sock.sendto(host.encode(), addr)
finally:
	sock.close()