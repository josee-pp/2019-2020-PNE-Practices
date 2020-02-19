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
    for i in range(number):
        whatever = pattern * (i+1)
        lst.append(whatever)
        print("New sequence created!")
    return lst

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print()
termcolor.cprint("List 1:", "blue")
termcolor.cprint(f"Sequence 0: (Length: {len(seq_list1[0])}) {seq_list1[0]}", "blue")
termcolor.cprint(f"Sequence 1: (Length: {len(seq_list1[1])}) {seq_list1[1]}", "blue")
termcolor.cprint(f"Sequence 2: (Length: {len(seq_list1[2])}) {seq_list1[2]}", "blue")

print()
termcolor.cprint("List 2:", "green")
termcolor.cprint(f"Sequence 0: (Length: {len(seq_list2[0])}) {seq_list2[0]}", "green")
termcolor.cprint(f"Sequence 1: (Length: {len(seq_list2[1])}) {seq_list2[1]}", "green")
termcolor.cprint(f"Sequence 2: (Length: {len(seq_list2[2])}) {seq_list2[2]}", "green")
termcolor.cprint(f"Sequence 3: (Length: {len(seq_list2[3])}) {seq_list2[3]}", "green")
termcolor.cprint(f"Sequence 4: (Length: {len(seq_list2[4])}) {seq_list2[4]}", "green")