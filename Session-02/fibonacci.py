a = 0
b = 1

n = int(input())

while a < n:
    print(a, end=" ")
    a = b
    b = a+b

print(a,b)



