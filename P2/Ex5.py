from pathlib import Path
from Client0 import Client
from termcolor import colored

folder = "/home/alumnos/joseepp/PycharmProjects/2019-2020-PNE-Practices/Session-04/"
dnafile = "U5.txt"
filename = folder + dnafile
file_contents = Path(filename).read_text()
bodystr = " "
lines = file_contents.split('\n')
body = lines[1:]
msg2 = bodystr.join(body).replace(" ", "")

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.253.169"
PORT = 8080

c = Client(IP, PORT)

msg1 = "Sending U5 Gene to the server..."


msglist = []
msglist.append(msg1)
msglist.append(msg2)

for a in msglist:
    print(f"To Server: {colored(a, 'blue')}")
    response = c.debug_talk(a)
    print(f"From Server: {response}")

