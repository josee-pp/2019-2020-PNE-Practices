# -- 1 + 2 + 3 + ... + 20
# -- 1 + ... + 100

def sumn(n):
    res = 0
    for i in range(1, n):
        res += i
    return res

userinput = int(input("Enter number n: "))
res20 = 0

for i in range(1,21):
    res20 += i

res100 = 0

for i in range(1, 101):
    res100 += i

print("sum of 1-", userinputm, "is: ", sumn(userinput))


