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

    def count_base(self, base):
        count = 0
        if self.strbases == "ERROR":
            return "0"
        elif self.strbases == "NULL":
            return "0"
        else:
            for element in self.strbases:
                if element == base:
                    count = count + 1
        return count

    def count(self,base):
        baselist = ["A", "C", "G", "T"]
        countlist=[]
        counterA = 0
        counterC = 0
        counterG = 0
        counterT = 0
        for i in self.strbases:
            if self.strbases == "NULL" or self.strbases == "ERROR":
                counterA = 0
                counterC = 0
                counterG = 0
                counterT = 0
                countlist.append(counterA)
                countlist.append(counterT)
                countlist.append(counterC)
                countlist.append(counterG)
                basedict = dict(zip(baselist, countlist))
                return basedict

            else:
                for i in self.strbases:
                    if i == "A":
                        counterA += 1
                    elif i == "C":
                        counterC += 1
                    elif i == "G":
                        counterG += 1
                    elif i == "T":
                        counterT += 1
                countlist.append(counterA)
                countlist.append(counterT)
                countlist.append(counterC)
                countlist.append(counterG)
                basedict = dict(zip(baselist, countlist))
                return basedict

    def reverse(self):
        if self.strbases == "NULL":
            return "NULL"
        elif self.strbases == "ERROR":
            return "ERROR"
        else:
            return (self.strbases[::-1])

    def complement(self):
        comp = ""
        if self.strbases == "NULL":
            return "NULL"
        elif self.strbases == "ERROR":
            return "ERROR"
        else:
            for i in self.strbases:
                if i == "A":
                    comp = comp + "T"
                elif i == "C":
                    comp = comp + "G"
                elif i == "G":
                    comp = comp + "C"
                elif i == "T":
                    comp = comp + "A"
                else:
                    next
            return comp
    pass