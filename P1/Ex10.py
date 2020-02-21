import operator
from Seq1 import Seq
from pathlib import Path

FOLDER = "/home/alumnos/joseepp/PycharmProjects/2019-2020-PNE-Practices/Session-04/"
FILENAME = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
BASES = ["A", "C", "G", "T"]

for element in FILENAME:
    dnafile = FOLDER + element + ".txt"
    s = Seq()
    s1 = Seq(s.read_fasta(dnafile))
    print("Gene", element + ":", " Most frequent base: ", s1.processing_genes(BASES))