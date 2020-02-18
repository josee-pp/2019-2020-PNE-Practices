class Seq:
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")
    def __str__(self):
        return self.strbases
    def len(self):
        return len(self.strbases)
    pass

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

# --- Main program
s1 = seq_list[0]
s2 = seq_list[1]
s3 = seq_list[2]
print(f"Sequence 1: (Length: {s1.len()}) {s1}")
print(f"Sequence 2: (Length: {s2.len()}) {s2}")
print(f"Sequence 3: (Length: {s3.len()}) {s3}")


