class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        self.strbases = strbases
        bases = []
        for i in self.strbases:
            if i == "A":
                bases.append(i)
            elif i == "C":
                bases.append(i)
            elif i == "G":
                bases.append(i)
            elif i == "T":
                bases.append(i)
            else:
                print("ERROR")
                break
        print("".join(bases))
    def __str__(self):
        return self.strbases

# --- Main program
s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")