def count_base(seq, base):
    count = 0
    for element in seq:
        if element == base:
            count = count + 1
    return count

sequence = "ACTGTC"
baselist = ["A", "C", "G", "T"]
countlist = []
perclist = []
for base in baselist:
    count = count_base(sequence, base)
    countlist.append(count)
    percentage = (count / len(sequence)) * 100
    perclist.append(f"({round(percentage, 2)} %)")
result = f"Total length: {len(sequence)}\n {baselist[0]}: {countlist[0]} {perclist[0]}\n {baselist[1]}: {countlist[1]} {perclist[1]}\n {baselist[2]}: {countlist[2]} {perclist[2]}\n {baselist[3]}: {countlist[3]} {perclist[3]}\n"
print(result)
