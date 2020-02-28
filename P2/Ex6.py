from pathlib import Path
from Client0 import Client
from Seq1 import Seq

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
    fraglist.append(frag1)
    fraglist.append(frag2)
    fraglist.append(frag3)
    fraglist.append(frag4)
    fraglist.append(frag5)
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
PORT = 8080

c = Client(IP, PORT)

msg = "Sending FRAT1 Gene to the server, in fragments of 10 bases..."

response = c.debug_talk(msg)
print(c)

fragments = seq_divider(filename)[0]
dnabody = seq_divider(filename)[1]

snull = Seq()

print(f"Gene FRAT1: {dnabody}")
for a in fragments:
    print(f"Fragment {fragments.index(a) + 1}: {a}")
    response = c.debug_talk(f"Fragment {fragments.index(a) + 1}: {a}")

