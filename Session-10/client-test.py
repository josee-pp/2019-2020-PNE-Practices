from Client0 import Client
from termcolor import colored

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

# -- Create the client object
c = Client(IP, PORT)
count = 0

# -- Each message is counted, and both message and response are printed. The program stops at the 5th message.
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