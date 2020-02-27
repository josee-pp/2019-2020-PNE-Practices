from pathlib import Path
from Client0 import Client

def seq_divider(filename):
    bodystr = ""
    file_contents = Path(filename).read_text()
    lines = file_contents.split('\n')
    body = lines[1:]
    bodystr = bodystr.join(body).replace(" ", "")
    fraglist = []
    frag1 = bodystr[0:10]
    frag2 = bodystr[10:20]
    frag3 = bodystr[20:30]
    frag4 = bodystr[30:40]
    frag5 = bodystr[40:50]
    frag6 = bodystr[50:60]
    frag7 = bodystr[60:70]
    frag8 = bodystr[70:80]
    frag9 = bodystr[80:90]
    frag10 = bodystr[90:100]
    fraglist.append(frag1)
    fraglist.append(frag2)
    fraglist.append(frag3)
    fraglist.append(frag4)
    fraglist.append(frag5)
    fraglist.append(frag6)
    fraglist.append(frag7)
    fraglist.append(frag8)
    fraglist.append(frag9)
    fraglist.append(frag10)
    return fraglist, bodystr

folder = "/home/alumnos/joseepp/PycharmProjects/2019-2020-PNE-Practices/Session-04/"
dnafile = "FRAT1.txt"
filename = folder + dnafile


from Client0 import Client
from termcolor import colored

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.253.169"

PORTLIST = []
PORT1 = 8080
PORT2 = 8081
PORTLIST.append(PORT1)
PORTLIST.append(PORT2)


c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)

fragments = seq_divider(filename)[0]
dnabody = seq_divider(filename)[1]

print(f"Gene FRAT1: {dnabody}")

for a in fragments:
    if (fragments.index(a) + 1) == 1 or 3 or 5 or 7 or 9:
        print(f"Fragment {fragments.index(a) + 1}: {a}")
        response = c1.talk(a)
    else:
        print(f"Fragment {fragments.index(a) + 1}: {a}")
        response = c2.talk(a)
