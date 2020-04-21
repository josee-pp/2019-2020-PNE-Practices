from Seq0 import *
from pathlib import Path

FOLDER = "/home/alumnos/joseepp/PycharmProjects/2019-2020-PNE-Practices/Session-04/"

FILENAME = "U5.txt"

# - - After defining the path of the filename containing the code
# we create the entire filename:
DNAFILE = FOLDER + FILENAME

print(DNAFILE)

# - - The function seq_read_fasta Open a DNA file in FASTA format and
# return the sequence as a string (It should only contains the characters 'A', 'T', 'G' or 'C:

print("DNA file: ", FILENAME)
print("The first 20 bases are: ", seq_read_fasta(DNAFILE))


