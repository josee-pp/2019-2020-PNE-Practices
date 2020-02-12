from Seq0 import *
from pathlib import Path

FOLDER = "/home/alumnos/joseepp/PycharmProjects/2019-2020-PNE-Practices/Session-04/"
FILENAME = ["U5", "ADA", "FRAT1", "FXN", "U5"]
BASES = ["A", "T", "C", "G"]

for element in FILENAME:
    dnafile = FOLDER + element + ".txt"
    BASESLIST = list(seq_count(dnafile))
    print("Gene", element, ":", dict(zip(BASES, BASESLIST)))