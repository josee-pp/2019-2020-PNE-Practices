from Seq0 import *
from pathlib import Path

FOLDER = "/home/alumnos/joseepp/PycharmProjects/2019-2020-PNE-Practices/Session-04/"
FILENAME = ["U5", "ADA", "FRAT1", "FXN", "U5"]
BASES = ["A", "T", "C", "G"]

for element in FILENAME:
    dnafile = FOLDER + element + ".txt"
    # seq_count function: Calculate the number of all the bases in the sequence.
    # A dictionary with the results is returned. The keys are the bases and the values their number.
    print("Gene", element, ":", seq_count(dnafile))
