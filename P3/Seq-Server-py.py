import socket
import termcolor
from Seq1 import Seq

# FUNCTIONS:

def PING():
    print("OK!")

def GET(n):
    seqlist = ["ATCGATCAGTCGATCG", "TAGCTACGATCAGACT", "CGTAGCTACGATAT", "GTACGATCTAGAGCT"]
    for seq in seqlist:
        return (f"{seqlist[n]}\n")


# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

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
            seq = msg.split(" ")[1]

