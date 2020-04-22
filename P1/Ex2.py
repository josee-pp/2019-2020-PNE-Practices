from Seq1 import Seq

# Create Null sequence:
snull = Seq()

# Create valid sequence:
svalid = Seq("TATAC")

seqlist = [snull, svalid]
for i in seqlist:
    print(f"Sequence {seqlist.index(i) + 1}: {i}")