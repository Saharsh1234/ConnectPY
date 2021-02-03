import socket


udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(("", 15000))
while True:
    data, addr = udp.recvfrom(4096)
    if data:
        print(data)
        break
udp.close()

UDP_IP = addr[0]
UDP_PORT = 10112
ADDR = (UDP_IP, UDP_PORT)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect(ADDR)
print(f"Connected to {UDP_IP} on {UDP_PORT}")
