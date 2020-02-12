from Seq0 import *
from pathlib import Path

FOLDER = "/home/alumnos/joseepp/PycharmProjects/2019-2020-PNE-Practices/Session-04/"

FILENAME = "U5.txt"
DNAFILE = FOLDER + FILENAME

print(DNAFILE)

print("DNA file: ", FILENAME)
print("The first 20 bases are: ", seq_read_fasta(DNAFILE))


