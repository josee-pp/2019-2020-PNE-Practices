# S2 E3

def fibosum(n):
    a = 0
    b = 1
    for i in range(n):
        a = b
        b = a + b
        return a+b

print(fibosum(5))

