from pathlib import Path
from Client0 import Client
from Seq1 import Seq

PORT = 8080
IP = "192.168.1.48"

c = Client(IP, PORT)

print(f"Connection to SERVER at {c.IP}, PORT: {c.PORT}")

while True:

    msg = input("Enter message: ")

    if msg == 'PING':
        print("* Testing PING...")
        response = c.talk(msg)
        print(response)

    elif 'GET' in msg:
        print("* Testing GET...")
        response = c.talk(msg)
        print(response)

    elif 'INFO' in msg:
        print("* Testing INFO...")
        response = c.talk(msg)
        print(response)

    elif 'COMP' in msg:
        print("* Testing COMP...")
        response = c.talk(msg)
        print(response)

    elif 'REV' in msg:
        print("* Testing REV...")
        response = c.talk(msg)
        print(response)

    elif 'GENE' in msg:
        print("* Testing GENE...")
        response = c.talk(msg)
        print(response)

    elif 'EXIT' in msg:
        exit()

