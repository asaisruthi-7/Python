n=int(input())
def count_digits(n):
    if n==0:
        return 1
    if n<0:
        n=-n
    count=0
    while n>0:
        count+=1
        n=n//10
    return count
print(count_digits(n))
