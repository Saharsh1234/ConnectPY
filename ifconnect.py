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
        break
udp.close()

UDP_IP = addr[0]
UDP_PORT = 10111
ADDR = (UDP_IP, UDP_PORT)

# Establish TCP Connection

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect(ADDR)
print(f'Connected to {UDP_IP} on {UDP_PORT}')

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
        return

# Input

while(requests <= 2000):
    if(keyboard.is_pressed('c') == True):
        command("Commands.ShowATCWindowCommand", [])
        time.sleep(0.50)
    elif(keyboard.is_pressed('f') == True):
        command("Commands.FlapsDown", [])
        time.sleep(0.50)
    elif(keyboard.is_pressed('g') == True):
        command("commands.landinggear",[])
        time.sleep(0.50)
    elif(keyboard.is_pressed('u') == True):
        command("commands.FlapsUp", [])
        time.sleep(0.50)
    elif(keyboard.is_pressed('z') == True):
        command("commands.spoilers", [])
        time.sleep(0.50)
    elif(keyboard.is_pressed('3') == True):
        command("commands.setflybycamera", [])
        time.sleep(0.50)
    elif(keyboard.is_pressed('1') == True):
        command("commands.setcockpitcamera", [])
        time.sleep(0.50)
    elif(keyboard.is_pressed('2') == True):
        command("commands.setvirtualcockpitcameracommand", [])
        time.sleep(0.50)
    elif(keyboard.is_pressed('4') == True):
        command("commands.setfollowcameracommand", [])
        time.sleep(0.50)
    elif(keyboard.is_pressed('5') == True):
        command("commands.settowercameracommand", [])
        time.sleep(0.50)
    elif(keyboard.is_pressed('p') == True):
        command("Commands.TogglePause", [])
        time.sleep(0.50)
    elif(keyboard.is_pressed('l') == True):
        command("commands.landinglights", [])
        time.sleep(0.50)
    elif(keyboard.is_pressed('b') == True):
        command("commands.beaconlights", [])
        time.sleep(0.50)
    elif(keyboard.is_pressed('n') == True):
        command("commands.navlights", [])
        time.sleep(0.50)
    elif(keyboard.is_pressed('m')):
        command("commands.strobelights", [])
        time.sleep(0.50)
    elif(keyboard.is_pressed('[') == True):
        command("commands.elevatortrimup", [])
        time.sleep(0.50)
    elif(keyboard.is_pressed(']') == True):
        command("commands.elevatortrimdown", [])
        time.sleep(0.50)
    elif(keyboard.is_pressed('w') == True):
        command("commands.throttleupcommand", [])
        time.sleep(0.05)
    elif(keyboard.is_pressed('s') == True):
        command("commands.throttledowncommand", [])
        time.sleep(0.05)
    elif(keyboard.is_pressed('r') == True):
        command("commands.reversethrust", [])
        time.sleep(0.05)
    elif(keyboard.is_pressed('a') == True):
        command("commands.autopilot.toggle", [])
        time.sleep(0.50)
    elif(keyboard.is_pressed('space') == True):
        command("commands.parkingbrakes", [])
        time.sleep(0.50)
    elif(keyboard.is_pressed('h') == True):
        command("commands.togglehud", [])
        time.sleep(0.50)
    elif(keyboard.is_pressed('esc') == True):
        quit()
