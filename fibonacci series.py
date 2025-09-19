n=int(input("enter the range"))
a=0
b=1
print("fibonacci series")
print(a)
print(b)
i=1
while(i<=n):
    sum=a+b
    a=b
    b=sum
    i=i+1
    print(sum)
