from pathlib import Path
from Client0 import Client
from Seq1 import Seq

PORT = 8080
IP = "192.168.1.48"

c = Client(IP, PORT)

nc = 0

while True:

    msg = input("Enter message: ")

    if nc<5:

        if msg == 'PING':
            nc += 1
            print("* Testing PING...")
            response = c.talk(msg)
            print(response)

        elif 'GET' in msg:
            nc += 1
            print("* Testing GET...")
            response = c.talk(msg)
            print(response)

        elif 'INFO' in msg:
            nc += 1
            print("* Testing INFO...")
            response = c.talk(msg)
            print(response)

        elif 'COMP' in msg:
            nc += 1
            print("* Testing COMP...")
            response = c.talk(msg)
            print(response)

        elif 'REV' in msg:
            nc += 1
            print("* Testing REV...")
            response = c.talk(msg)
            print(response)

        elif 'GENE' in msg:
            nc += 1
            print("* Testing GENE...")
            response = c.talk(msg)
            print(response)

    else:
        exit()

