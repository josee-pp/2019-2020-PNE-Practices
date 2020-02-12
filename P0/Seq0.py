def seq_ping():
    print("OK!")

from pathlib import Path

def seq_read_fasta(filename):
    bodystr = ""
    file_contents = Path(filename).read_text()
    lines = file_contents.split('\n')
    body = lines[1:]
    bodystr = bodystr.join(body).replace(" ", "")
    return (bodystr[0:20])

def seq_len(seq):
    file_contents = Path(seq).read_text()
    bodystr = ""
    lines = file_contents.split('\n')
    body = lines[1:]
    bodystr = bodystr.join(body).replace(" ", "")
    return (len(bodystr))

def seq_count_base(seq, base):
    count = 0
    file_contents = Path(seq).read_text()
    seq = ""
    lines = file_contents.split('\n')
    body = lines[1:]
    seq = seq.join(body).replace(" ", "")
    for i in seq:
        if i == base:
            count += 1
    return (count)

def seq_count(seq):
    file_contents = Path(seq).read_text()
    seq = ""
    lines = file_contents.split('\n')
    body = lines[1:]
    seq = seq.join(body).replace(" ", "")
    countA = 0
    countT = 0
    countC = 0
    countG = 0
    for i in seq:
        if i == "A":
            countA = countA + 1
        elif i == "T":
            countT = countT + 1
        elif i == "C":
            countC = countC + 1
        elif i == "G":
            countG = countG + 1
        else:
            next
    return countA, countT, countC, countG




