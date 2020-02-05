def countbase(sequence):
    countA = 0
    countC = 0
    countG = 0
    countT = 0
    for i in sequence:
        if i == "A":
            countA = countA + 1
        elif i == "C":
            countC = countC + 1
        elif i == "G":
            countG = countG + 1
        elif i == "T":
            countT = countT + 1
        else:
            next
    return countA, countC, countG, countT

print(countbase("CATGTAGACTAG"))

