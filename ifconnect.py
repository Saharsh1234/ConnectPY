import socket
import json

localport = 10112
localip = 127.0.0.1

ifudp = socket.socket(socket.AF_IFNET, socket.SOCK_DGRAM)
ifupd.bind(("", 15000))
