class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        self.strbases = strbases
        for i in strbases:
            if i == "A" or "C" or "G" or "T":
                print("New sequence created!")
            else:
                break

    def __str__(self):
        return self.strbases

    pass


# --- Main program
s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")