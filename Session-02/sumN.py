# -- 1 + 2 + 3 + ... + 20
# -- 1 + ... + 100

def sumn(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res

userinput = int(input("Enter number n: "))

print("sum of 1-", userinput, "is: ", sumn(userinput))


