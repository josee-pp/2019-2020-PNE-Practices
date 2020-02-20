from Seq1 import Seq

snull = Seq()
svalid = Seq("TATAC")

seqlist = [snull, svalid]
for i in seqlist:
    print(f"Sequence {seqlist.index(i) + 1}: {i}")