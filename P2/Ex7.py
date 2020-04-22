from pathlib import Path
from Client0 import Client
from Seq1 import Seq

def seq_divider(filename):

    # -- Using the path function, we obtain the body of the filename, which is the gene code.
    bodystr = ""
    file_contents = Path(filename).read_text()
    lines = file_contents.split('\n')
    body = lines[1:]
    bodystr = bodystr.join(body).replace(" ", "")

    # -- We create lists of odd and even elements of the main list of fragments, and we define the fragments:
    fraglistodd = []
    fraglisteven = []
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

    # -- Odd and even lists:
    fraglistodd.append(frag1)
    fraglisteven.append(frag2)
    fraglistodd.append(frag3)
    fraglisteven.append(frag4)
    fraglistodd.append(frag5)
    fraglisteven.append(frag6)
    fraglistodd.append(frag7)
    fraglisteven.append(frag8)
    fraglistodd.append(frag9)
    fraglisteven.append(frag10)

    # -- All fragments list:
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

    # -- This function returns as a tuple the list of all fragments, the odd ones, the even ones and the entire body
    # of the sequence:
    return fraglist, fraglistodd, fraglisteven, bodystr

folder = "/home/alumnos/joseepp/PycharmProjects/2019-2020-PNE-Practices/Session-04/"
dnafile = "FRAT1.txt"
filename = folder + dnafile


PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the servers to talk to:
IP = "212.128.253.169"  # -- Same IP but...

# -- Different ports:

PORTLIST = []
PORT1 = 8080
PORT2 = 8081
PORTLIST.append(PORT1)
PORTLIST.append(PORT2)

# -- Create a client object for each port:

c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)

allfragments = seq_divider(filename)[0]  # -- The first element corresponds to the full list of fragments
oddlist = seq_divider(filename)[1]       # -- List of odd elements of the allfragments list
evenlist = seq_divider(filename)[2]      # -- List of even elements of the allfragments list
dnabody = seq_divider(filename)[3]       # -- Full sequence

# -- We create a list of client objects, corresponding to the servers which we are going to interact to:
clientlist = []
clientlist.append(c1)
clientlist.append(c2)

msg = "Sending FRAT1 Gene to the server, in fragments of 10 bases..."

# -- We send the first message and the full body to both servers:

for client in clientlist:
    response = client.debug_talk(msg)
    print(client)

snull = Seq()

print(f"Gene FRAT1: {dnabody}")

for seq in allfragments:
    print(f"Fragment {allfragments.index(seq) + 1}: {seq}")

# -- Odd elements go to server 1:

for seq in oddlist:
    response = c1.debug_talk(f"Fragment {allfragments.index(seq) + 1}: {seq}")

# -- Even elements go to server 2:

for seq in evenlist:
    response = c2.debug_talk(f"Fragment {allfragments.index(seq) + 1}: {seq}")
