import socket
from termcolor import colored
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
        percentage = round((count/seqlen)*100, 2)
        percentlist.append(percentage)
    return (seq, seqlen, countlist, percentlist)





# Configure the Server's IP and PORT
PORT = 8080
IP = "192.168.1.48"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("SEQ Server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for clients...")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:
        print("A client has connected to the server!")
        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()

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
