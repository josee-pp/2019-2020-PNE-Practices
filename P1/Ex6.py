from Seq1 import Seq

baselist = ["A", "C", "T", "G"]

# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

seqlist = [s1, s2, s3]
baselist = ["A", "C", "G", "T"]
for i in seqlist:
    print(f"Sequence {seqlist.index(i)}, (Length: {i.len()}) {i} \n {i.count(baselist)}")
