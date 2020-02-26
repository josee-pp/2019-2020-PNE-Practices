from Client0 import Client
from termcolor import colored

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.253.169"
PORT = 8080

c = Client(IP, PORT)

msg1 = "Message 1---"
msg2 = "Testing!!!"

msglist = []
msglist.append(msg1)
msglist.append(msg2)

for a in msglist:
    print(f"To Server: {colored(a, 'blue')}")
    response = c.debug_talk(a)
    print(f"From Server: {response}")
