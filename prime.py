flag=0
n=int(input())
for i in range(2,n):
    if n%i==0:
        flag=1
        break
if flag==0:
    print("valid")
else:
    print("invalid")