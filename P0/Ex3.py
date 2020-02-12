from Seq0 import *
from pathlib import Path

FOLDER = "/home/alumnos/joseepp/PycharmProjects/2019-2020-PNE-Practices/Session-04/"
FILENAME = ["U5", "ADA", "FRAT1", "FXN", "U5"]

for i in FILENAME:
    FILENAME2 = FOLDER + i + ".txt"
    print(seq_len(FILENAME2))