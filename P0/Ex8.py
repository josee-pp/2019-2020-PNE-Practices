from Seq0 import *
from pathlib import Path
import operator

FOLDER = "/home/alumnos/joseepp/PycharmProjects/2019-2020-PNE-Practices/Session-04/"
FILENAME = ["U5", "ADA", "FRAT1", "FXN", "U5"]
BASES = ["A", "C", "T", "G"]

for element in FILENAME:
    dnafile = FOLDER + element + ".txt"
    sorted_dict = sorted(seq_count(dnafile).items(), key=operator.itemgetter(1))
    frequentb = sorted_dict[-1]
    print("Gene", element + ":", " Most frequent base: ", frequentb[0])