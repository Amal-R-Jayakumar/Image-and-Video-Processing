n,m=map(int,input("Interval(Enter them separated by space): ").split())
if n>m:
    n,m=m,n
list_1=[]
if n<=1:
    n=2
for i in range(n,m):
    for j in range(2, i//2+1):
        if i%j == 0:
            break
    else:
        list_1.append(str(i))
print(" ".join(list_1))