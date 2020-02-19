from Seq1 import Seq

def print_seq(seq_list):
    for element in seq_list:
        seq = seq_list[seq_list.index(element)]
        print(f"Sequence: {seq_list.index(element)} (Length: {len(seq)}) {seq}")

seq = Seq("ACTGA")
print(f"Sequence 1: (Length: {seq.len()}) {seq}")