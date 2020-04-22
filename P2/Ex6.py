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

    # -- We create a fragments list of 5 elements (fragments), each one with 10 characters (bases):
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

    # -- This function returns the list of fragments and the entire body as a tuple:
    return fraglist, bodystr


folder = "/home/alumnos/joseepp/PycharmProjects/2019-2020-PNE-Practices/Session-04/"
dnafile = "FRAT1.txt"
filename = folder + dnafile

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.253.171"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

# -- We define the first message and its response:
msg = "Sending FRAT1 Gene to the server, in fragments of 10 bases..."
response = c.debug_talk(msg)
print(c)

fragments = seq_divider(filename)[0] # -- The first element of the tuple corresponds to the list of fragments.
dnabody = seq_divider(filename)[1] # -- The second element corresponds to the full code.

snull = Seq()

print(f"Gene FRAT1: {dnabody}")

# -- We send each fragment to the server:
for a in fragments:
    print(f"Fragment {fragments.index(a) + 1}: {a}")
    response = c.debug_talk(f"Fragment {fragments.index(a) + 1}: {a}")

