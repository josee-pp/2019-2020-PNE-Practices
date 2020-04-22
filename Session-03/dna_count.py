def countbase(sequence):
    countA = 0
    countC = 0
    countG = 0
    countT = 0

    # -- If the element of the sequence matches with a base, the count of that base increases.
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

    # -- The length will be the sum of the counts.
    length = countA + countC + countG + countT
    return length, countA, countC, countG, countT

print("Total number of bases", countbase("CATGTAGACTAG")[0])
print("A: ", countbase("CATGTAGACTAG")[1])
print("C: ", countbase("CATGTAGACTAG")[2])
print("G: ", countbase("CATGTAGACTAG")[3])
print("T: ", countbase("CATGTAGACTAG")[4])

