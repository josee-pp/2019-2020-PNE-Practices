from Client0 import Client
from termcolor import colored


IP = "192.168.1.48"
PORT = 8080

c = Client(IP, PORT)

while True:
    msg = input()
    msgtoserver = colored(msg, "blue")
    print(f"To Server: {msgtoserver}")
    msgfromserver = colored(msg, "green")
    response = c.debug_talk(msgfromserver)
    print(f"From Server: {response}")