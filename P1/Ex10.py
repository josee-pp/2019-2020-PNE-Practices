import operator
from Seq1 import Seq
from pathlib import Path

FOLDER = "C:/Users/José/PycharmProjects/2019-2020-PNE-Practices/Session-04/"
FILENAME = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
BASES = ["A", "C", "T", "G"]

for element in FILENAME:
    dnafile = FOLDER + element + ".txt"
    s = Seq(dnafile)
    sorted_dict = sorted((s.count(BASES)).items(), key=operator.itemgetter(1))
    frequentb = sorted_dict[-1]
    print("Gene", element + ":", " Most frequent base: ", frequentb[0])