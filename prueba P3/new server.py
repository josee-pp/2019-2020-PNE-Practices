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
    # In this function, we return, in order, as a tuple:
    # the sequence, its length, the counter of each of its bases and its base percentage conformation.

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

    # Finally, we return a tuple of 4 elements:
    # sequence, sequence length, base count list and base percentage list.
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

nc = 0
client_ip_list = []


while True:
    if nc < 5:
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

            nc += 1
            client_ip_list.append(f'Client{nc}:{client_ip_port}')
            print("CONNECTION: {} From the IP: {}".format(nc, client_ip_port))

            # -- Read the message from the client
            # -- The received message is in raw bytes
            msg_raw = cs.recv(2048)

            # -- We decode it for converting it
            # -- into a human-redeable string
            msg = msg_raw.decode()

            if msg == "PING":
                print("PING command!")
                # -- Send a response message to the client
                ping()
                cs.close()

            elif msg.split(" ")[0] == "GET":
                number = int(msg.split(" ")[1])
                response = f"GET {number}\n{str(get(number))}"
                cs.send(response.encode())
                cs.close()

            elif msg.split(" ")[0] == "INFO":
                seq = msg.split(" ")[1]
                seqlen = info(seq)[1]
                countlist = info(seq)[2]
                percentlist = info(seq)[3]
                response = f"Sequence: {seq}\nTotal length: {seqlen}\nA: {countlist[0]} ({percentlist[0]}%)\nC: {countlist[1]} ({percentlist[1]}%)\nG: {countlist[2]} ({percentlist[2]}%)\nT: {countlist[3]} ({percentlist[3]}%)\n"
                cs.send(response.encode())
                cs.close()

            elif msg.split(" ")[0] == "COMP":
                seq = msg.split(" ")[1]
                s = Seq(seq)
                comp = s.complement()
                response = f"COMP {seq}\n{comp}"
                cs.send(response.encode())
                cs.close()

            elif msg.split(" ")[0] == "REV":
                seq = msg.split(" ")[1]
                s = Seq(seq)
                rev = s.reverse()
                response = f"REV {seq}\n{rev}"
                cs.send(response.encode())
                cs.close()

            elif msg.split(" ")[0] == "GENE":
                filename = msg.split(" ")[1]
                doclist = ['U5', 'ADA', 'FRAT1', 'FXN', 'RNU6_269P']
                FOLDER = "/home/alumnos/joseepp/PycharmProjects/2019-2020-PNE-Practices/Session-04/"
                for element in doclist:
                    if filename == element:
                        dnafile = FOLDER + filename + ".txt"
                s = Seq()
                s1 = Seq(s.read_fasta(dnafile))
                response = f"{msg}\n{s1}"
                cs.send(response.encode())
                cs.close()
    else:
        print(f'The following clients have sended a message to the server:')
        for i in client_ip_list:
            print(i)
        ls.close()
        exit()











