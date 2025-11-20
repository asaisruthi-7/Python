n=int(input())
c=0
for i in range(1,int(n**0.5)+1):
    if(n%i==0):
        c=c+1
        if(i!=n//i):
            c=c+1
if(c==2):
    print("Pime number")
else:
    print("Not a Prime Number")
