# S2 E2

def fibon(n):
    if n+1 < 0:
        print("Incorrect input")
    elif n+1 == 1:
        return 0
    elif n+1 == 2:
        return 1
    else:
        return fibon(n-1) + fibon(n-2)

print(fibon(5))
print(fibon(10))
print(fibon(15))
