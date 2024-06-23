def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter the number to find its factorial "))
for i in range(n):
    print(fact(n))