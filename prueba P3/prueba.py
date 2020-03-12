import socket
import termcolor
from Seq1 import Seq

# FUNCTIONS:

def PING():
    print("OK!")

seqlist = ["ATCGATCAGTCGATCG", "TAGCTACGATCAGACT", "CGTAGCTACGATAT", "GTACGATCTAGAGCT"]
def GET(n):
    for seq in seqlist:
        if n == seqlist.index(seq):
            return seq

def INFO(seq):
    s = Seq(seq)
    seqlen = s.len()
    counti = 0
    baseslist = ["A", "C", "G", "T"]
    countlist = []
    percentlist = []
    for i in seq:
        if i in baseslist:
            counti = counti + 1
        countlist.append(counti)
    for count in countlist:
        percentage = (count/seqlen)*100
        percentlist.append(percentage)
    return (seq, seqlen, countlist, percentlist)

msg = input("Enter message: ")

while True:
    if msg == "PING":
        # -- Print the received message
        termcolor.cprint("PING command!", "yellow")
        PING()
        # -- Send a response message to the client
        response = "OK!\n"
        # -- The message has to be encoded into bytes
        cs.send(response.encode())
        # -- Close the data socket
        cs.close()

    elif msg.split(" ")[0] == "GET":
        number = int(msg.split(" ")[1])
        response = str(GET(number))
        print(f"GET\n{response}")
        cs.send(response.encode())
        cs.close()

    elif msg.split(" ")[0] == "INFO":
        baseslist = ["A", "C", "G", "T"]
        seq = msg.split(" ")[1]
        seqlen = INFO(seq)[1]
        countlist = INFO(seq)[2]
        percentlist = INFO(seq)[2]
        print(INFO(seq))
