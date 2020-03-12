from Client0 import Client
from termcolor import colored


IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
count = 0

while True:
    msg = f"Message {count}"
    msgtoserver = colored(msg, "blue")
    print(f"To Server: {msgtoserver}")
    msgfromserver = colored(msg, "green")
    response = c.debug_talk(msgfromserver)
    print(f"From Server: {response}")
    count = count + 1
    if count == 5:
        break