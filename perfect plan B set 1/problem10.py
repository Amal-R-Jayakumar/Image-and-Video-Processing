#Method 1
list1=['0','1']
def fib0(n):
    k=1
    m=0
    global list1
    for _ in range(n-1):
        n1=m+k
        list1.append(str(n1))
        k,m=n1,k
    return " ".join(list1)

#print(fib0 (int(input())))


list1.clear()
list1=['0']
#This code is taking a lot of time.
def fib1(n):
    if n==0 or n==1:
        return n
    recc_fib=fib1(n-1)+fib1(n-2)
    return recc_fib


for i in range(int(input())):

    list1.append(str(fib1 (i+1)))
    
print(" ".join(list1))
