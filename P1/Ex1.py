from Seq1 import Seq

seq_list = [Seq("ACTGA")]
for element in seq_list:
    print(f"Sequence: {seq_list.index(element)+1} (Length: {element.len()}) {seq}")
