class Seq:
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")
    def __str__(self):
        return self.strbases
    def len(self):
        return len(self.strbases)
    pass

def print_seq(seq_list):
    for element in seq_list:
        seq = seq_list[seq_list.index(element)]
        print(f"Sequence: {seq_list.index(element)} (Length: {seq.len()}) {seq}")

# --- Main program

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

print_seq(seq_list)


