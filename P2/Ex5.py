from pathlib import Path
from Client0 import Client
from termcolor import colored

folder = "/home/alumnos/joseepp/PycharmProjects/2019-2020-PNE-Practices/Session-04/"
dnafile = "U5.txt"

# -- We create the entire filename
filename = folder + dnafile

# -- An then, using the path function, we extract the body of the text, which is the gene code. In this case, the code
# will be the second message to be sent:

file_contents = Path(filename).read_text()
bodystr = " "
lines = file_contents.split('\n')
body = lines[1:]
msg2 = bodystr.join(body).replace(" ", "")

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.253.169"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

msg1 = "Sending U5 Gene to the server..."

# -- List of messages:
msglist = []
msglist.append(msg1)
msglist.append(msg2)

# -- Each message will be sent, and the server will give us a response.
for a in msglist:
    print(f"To Server: {colored(a, 'blue')}")
    response = c.debug_talk(a)
    print(f"From Server: {response}")

