from Seq0 import *
from pathlib import Path

FOLDER = "/home/alumnos/joseepp/PycharmProjects/2019-2020-PNE-Practices/Session-04/"
FILENAME = ["U5", "ADA", "FRAT1", "FXN", "U5"]

# We print the length for each sequence of the list FILENAME:

for i in FILENAME:
    dnafile = FOLDER + i + ".txt"
    # - - The seq_len function Calculate the total number of bases in the sequence:
    print("Gene", i, "---> Length: ", seq_len(dnafile))