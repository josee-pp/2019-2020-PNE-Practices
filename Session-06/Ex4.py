import termcolor

class Seq:
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")
    def __str__(self):
        return self.strbases
    def len(self):
        return len(self.strbases)
    pass

def generate_seqs(pattern, number):
    lst = []
    base = ""
    for i in range(1, number + 1):
        base = pattern * i
        lst.append(base)
        print("New sequence created!")
    return lst

def print_seq(seq_list, color):
    for element in seq_list:
        seq = seq_list[seq_list.index(element)]
        termcolor.cprint(f"Sequence: {seq_list.index(element)} (Length: {len(seq)}) {seq}", color)


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print()
termcolor.cprint("List 1:", "blue")
print_seq(seq_list1, "blue")

print()
termcolor.cprint("List 2:", "green")
print_seq(seq_list2, "green")