from Seq0 import *
from pathlib import Path

FOLDER = "/home/alumnos/joseepp/PycharmProjects/2019-2020-PNE-Practices/Session-04/"
FILENAME = ["U5", "ADA", "FRAT1", "FXN", "U5"]
BASES = ["A", "C", "T", "G"]

# - - For each gene (element of FILENAME list) we print its name and we obtain the
# entire filename (dnafile):

for element in FILENAME:
    dnafile = FOLDER + element + ".txt"
    print("Gene: " + element)
    # For each base we count it using seq_count_base:
    for i in BASES:
        print(i + ":", seq_count_base(dnafile, i))