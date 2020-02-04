
n=int(input("Enter the terms"))
a=0
b=1

if n<=0:
    print("The requested series is",f)
else:
    print(a,b,end=" ")
    for x in range(2,n):
        next=a+b
        print(next,end=" ")
        a=b
        b=next


