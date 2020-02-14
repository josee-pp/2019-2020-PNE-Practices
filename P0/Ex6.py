from Seq0 import *
from pathlib import Path

FOLDER = "/home/alumnos/joseepp/PycharmProjects/2019-2020-PNE-Practices/Session-04/"

FILENAME = "U5.txt"
DNAFILE = FOLDER + FILENAME

print("Gene U5: ")
print("Frag: ", seq_read_fasta(filename)[0])
print("Rev: ", seq_reverse(filename)[1])