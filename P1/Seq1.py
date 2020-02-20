class Seq:
    def __init__(self, strbases=None):
        self.strbases = strbases
        baselist = ["A", "C", "G", "T"]
        cancontinue = ""
        if strbases == None:
            print("NULL Seq created!")
            self.strbases = "NULL"
        else:
            for element in strbases:
                if element not in baselist:
                    cancontinue = "False"
                elif element in baselist:
                    cancontinue = "True"
            if cancontinue == "False":
                print("INVALID Seq!")
                self.strbases = "ERROR"
            elif cancontinue == "True":
                print("New sequence created!")
    def __str__(self):
        return self.strbases
    def len(self):
        if self.strbases == "ERROR":
            return "0"
        elif self.strbases == "NULL":
            return "0"
        else:
            return len(self.strbases)
    pass