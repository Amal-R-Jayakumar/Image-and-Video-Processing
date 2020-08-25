#Method 1
def fib0(n):
    k=1
    m=0
    for _ in range(n-1):
        n1=m+k
        k,m=n1,k
    return n1

#This code is taking a lot of time.
def fib1(n):
    if n==0 or n==1:
        return n
    recc_fib=fib1(n-1)+fib1(n-2)
    return recc_fib
#print(fib1 (int(input())))
print(fib0 (int(input())))