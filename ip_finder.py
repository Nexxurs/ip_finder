#!/usr/bin/env python3


class Pi:
    def __init__(self, ip, hostname):
        self.ip = ip
        self.hostname = hostname

    def __str__(self):
        return "{}: {}".format(self.hostname, self.ip)


def find_pis():
    import socket

    IP = "<broadcast>"
    PORT = 17155
    MESSAGE = "getPI"

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(MESSAGE.encode(), (IP, PORT))
    sock.settimeout(1)

    pis = []

    try:
        while True:
            data, (ip, port) = sock.recvfrom(1024)
            pi = Pi(ip, data.decode())
            pis.append(pi)
    except socket.timeout:
        pass
    finally:
        sock.close()
        return pis


if __name__ == '__main__':
    print(*find_pis(), sep='\n')
    input("Press Enter to Close")
