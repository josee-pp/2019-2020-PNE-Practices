class Seq:
    def __init__(self, strbases="NULL"):
        self.strbases = strbases
        if strbases == "NULL":
            print("NULL Seq created!")
        else:
            print("New sequence created!")
    def __str__(self):
        return self.strbases
    def len(self):
        return len(self.strbases)
    pass