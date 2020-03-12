import socket
from termcolor import colored
from Seq1 import Seq

# ----------- Functions:

def ping():
    response = "OK!\n"
    print(response)
    # We send to the client the OK! response:
    return cs.send(str.encode(response))

def get(n):
    seqlist = ["ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA", "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA", "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT", "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA", "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"]
    # We print all the sequences of the list:
    for sequence in seqlist:
        print(f"GET {seqlist.index(sequence)}: {sequence}")
    # Given the number of the sequence, we respond with that sequence:
    for sequence in seqlist:
        return seqlist[n]

def info(seq):
    # In this function, we return, in order, as a tuple: the sequence, its length, the counter of each of its bases and its base percentage conformation.

    # Length of the sequence:
    seqlen = len(seq)

    # Number of each of its bases:
    countA = 0
    countC = 0
    countG = 0
    countT = 0
    countlist = []
    for i in seq:
        if i == "A":
            countA = countA + 1
        elif i == "C":
            countC = countC + 1
        elif i == "G":
            countG = countG + 1
        elif i == "T":
            countT = countT + 1
        else:
            next
    # Now, we append each counter to the list of counters:
    countlist.append(countA)
    countlist.append(countC)
    countlist.append(countG)
    countlist.append(countT)

    # Percentage base conformation:
    percentlist = []
    for count in countlist:
        percentage = (count / seqlen) * 100
        percentage = round(percentage, 2)
        percentlist.append(percentage)

    # Finally, we return a tuple of 4 elements: sequence, sequence length, base count list and base percentage list.
    return (seq, seqlen, countlist, percentlist)

# ---------- SERVER:

# Configure the Server's IP and PORT
PORT = 8080
IP = "192.168.1.48"

# Create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# Configure the socket for listening
ls.listen()

print("SEQ server configured!")













