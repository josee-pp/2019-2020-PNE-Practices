# S2 E2

def fibon(n):
    a = 0
    b = 1
    for i in range(n):
        c = a+b
        a = b
        b = c
    return a

print(fibon(5))
print(fibon(10))
print(fibon(15))
