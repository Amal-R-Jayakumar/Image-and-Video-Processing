import math
#Method 1
def checkFib1(n):
    k=1
    m=0
    for _ in range(n):
        n1=m+k
        k,m=n1,k
        if n1==n:
            print("yes")
            break
    else:
        print("No")

#Method 2 - This won't work for bigger numbers
def checkFib0(n):
    x1 = 5*n**2+4
    x2 = 5*n**2-4
    root1=math.sqrt(x1)
    root2=math.sqrt(x2)
    if root1**2==x1 or root2**2==x2:
        print(root1)
        print(root2)
        return "Yes"
    else:
        print(round(root1**2),x1)
        print(round(root2**2),x2)
        return "No"

#print(checkFib0(int(input())))

checkFib1(int(input()))