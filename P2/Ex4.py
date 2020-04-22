from Client0 import Client
from termcolor import colored

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.253.169"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

# -- Now we define both messages:
msg1 = "Message 1"
msg2 = "Testing!!!"

# -- And create a list of messages:
msglist = []
msglist.append(msg1)
msglist.append(msg2)

# -- For each message of the list, it will be sent to the server, which for each message will give a response:
for a in msglist:
    print(f"To Server: {colored(a, 'blue')}")
    response = c.debug_talk(a)
    print(f"From Server: {response}")
