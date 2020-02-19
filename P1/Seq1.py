class Seq:
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")
    def __str__(self):
        return self.strbases
    def len(self):
        return len(self.strbases)
    pass