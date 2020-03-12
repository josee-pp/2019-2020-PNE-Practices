from Seq1 import Seq

seqlist = ["ATCGATCAGTCGATCG", "TAGCTACGATCAGACT", "CGTAGCTACGATAT", "GTACGATCTAGAGCT"]
def GET(n):
    for seq in seqlist:
        if n == seqlist.index(seq):
            return seq

def INFO(seq):
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
    countlist.append(countA)
    countlist.append(countC)
    countlist.append(countG)
    countlist.append(countT)
    seqlen = len(seq)
    percentlist = []
    for count in countlist:
        percentage = (count/seqlen)*100
        percentage = round(percentage, 2)
        percentlist.append(percentage)
    return (seq, seqlen, countlist, percentlist)

msg = input("Enter message: ")

while True:
    if msg == "PING":
        print("PING command!")
        # -- Send a response message to the client
        response = "OK!\n"
        print(response)
        break

    elif msg.split(" ")[0] == "GET":
        number = int(msg.split(" ")[1])
        response = str(GET(number))
        print(f"GET\n{response}")
        break

    elif msg.split(" ")[0] == "INFO":
        seq = msg.split(" ")[1]
        seqlen = INFO(seq)[1]
        countlist = INFO(seq)[2]
        percentlist = INFO(seq)[3]
        print(f"Sequence: {seq}\nTotal length: {seqlen}\nA: {countlist[0]} ({percentlist[0]}%)\nC: {countlist[1]} ({percentlist[1]}%)\nG: {countlist[2]} ({percentlist[2]}%)\nT: {countlist[3]} ({percentlist[3]}%)\n")
        break

    elif msg.split(" ")[0] == "COMP":
        seq = msg.split(" ")[1]
        s = Seq(seq)
        comp = s.complement()
        print(comp)
        break

    elif msg.split(" ")[0] == "REV":
        seq = msg.split(" ")[1]
        s = Seq(seq)
        rev = s.reverse()
        print(rev)
        break

    elif msg.split(" ")[0] == "GENE":
        filename = msg.split(" ")[1]
        FOLDER = "/home/alumnos/joseepp/PycharmProjects/2019-2020-PNE-Practices/Session-04/"
        dnafile = FOLDER + filename + ".txt"
        s = Seq()
        s1 = Seq(s.read_fasta(dnafile))
        print(s1)
        break

