from Seq1 import Seq
from pathlib import Path

FOLDER = "C:/Users/José/PycharmProjects/2019-2020-PNE-Practices/Session-04/"

FILE = "U5.txt"
FILENAME = FOLDER + FILE
baselist = ["A", "C", "G", "T"]

s = Seq()
s1 = Seq(s.read_fasta(FILENAME))

print(f"Sequence: (Length: {len(s.read_fasta(FILENAME))}) {s.read_fasta(FILENAME)} \n Bases: {s1.count(baselist[0])} \n Rev: {s1.reverse()} \n Comp: {s1.complement()}")


