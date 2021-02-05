# Imports

import socket
import json
from binascii import unhexlify
import keyboard
import time

requests = 0

# Establish UDP Connection

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(("", 15000))
while True:
    data, addr = udp.recvfrom(4096)
    if data:
        print(data)
        break
udp.close()

UDP_IP = addr[0]
UDP_PORT = 10111
ADDR = (UDP_IP, UDP_PORT)

# Establish TCP Connection

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect(ADDR)
print(f"Connected to {UDP_IP} on {UDP_PORT}")

# Send Commands to Infinite Flight

def command(cmd, param, await_response=False):
    commands_request = {"Command":cmd,"Param":param}
    commands_request = json.dumps(commands_request).encode("utf-8")
    req = unhexlify(hex(len(commands_request))[2:])
    request = req + b"\x00\x00\x00" + commands_request
    tcp.sendall(request)
    if await_response:
        response = tcp.recv(10)
        return response
    else:
        print("Request sent.")

# Input

while(requests <= 2000):
    print('A - ATC Window, F - Flaps Down, U - Flaps Up, G - Gear Down/Up, Q - Quit application ')
    if(keyboard.is_pressed('a') == True):
        command("Commands.ShowATCWindowCommand", [])
        time.sleep(1)
    elif(keyboard.is_pressed('f') == True):
        command("Commands.FlapsDown", [])
        time.sleep(1)
    elif(keyboard.is_pressed('g') == True):
        command("commands.landinggear",[])
        time.sleep(1)
    elif(keyboard.is_pressed('u') == True):
        command("commands.FlapsUp", [])
        time.sleep(1)
    elif(keyboard.is_pressed('q') == True):
        quit()
    else:
        input1 = input('What would you like to do?')
