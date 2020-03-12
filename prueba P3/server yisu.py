import socket
from termcolor import colored
from Seq1 import Seq

#GET function
list_seq=["ACGCCTAGTCA","ACTGAATGGACTCAG","TTGCATGGCAAGCT","CGGTAAGCTACG","GTCCGAATGCAT"]
def GET_FUNCTION(n):
    for i in list_seq:
        if n ==list_seq.index(i):
            return i
#INFO function
BASE_list=["A","C","T","G"]
def INFO_FUNCTION(seq):
    seq= Seq(seq)
    return seq.count(BASE_list)



# Configure the Server's IP and PORT
PORT = 8080
IP = "192.168.1.48"
list_seq=["ACGCCTAGTCA","ACTGAATGGACTCAG","TTGCATGGCAAGCT","CGGTAAGCTACG","GTCCGAATGCAT"]
# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

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
            print(colored("PING COMMAND","green"))
            response = "OK!\n"
            cs.send(response.encode())
            cs.close()
        elif msg.split(" ")[0]=="GET":
            print(colored("GET COMMAND", "green"))
            n= int(msg.split(" ")[1])
            response= GET_FUNCTION(n)
            cs.send(response.encode())
            cs.close()
        elif msg.split(" ")[0]=="INFO":
            print(colored("INFO COMMAND", "green"))
            n = msg.split(" ")[1]
            response = INFO_FUNCTION(n)
            [[key, value]] = ((str(key), str(value)) for key, value in response.items())
            response= key + ":" + value
            cs.send(response.encode())
            cs.close()