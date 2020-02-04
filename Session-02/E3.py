# S2 E3

def fibosum(n):
    a = 0
    b = 1
    d = 0
    for i in range(n):
        c = a + b
        a = b
        b = c
        d = d + a
    return d

print(fibosum(5))
print(fibosum(10))

