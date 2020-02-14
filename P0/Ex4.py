from Seq0 import *
from pathlib import Path

FOLDER = "/home/alumnos/joseepp/PycharmProjects/2019-2020-PNE-Practices/Session-04/"
FILENAME = ["U5", "ADA", "FRAT1", "FXN", "U5"]
BASES = ["A", "C", "T", "G"]

for element in FILENAME:
    dnafile = FOLDER + element + ".txt"
    print("Gene: "+ element)
    for i in BASES:
        print(i+":", seq_count_base(dnafile, i))