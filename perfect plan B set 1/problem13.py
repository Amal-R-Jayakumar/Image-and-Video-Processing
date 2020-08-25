#Method 1
def squareSum0(n):
    return n*(n+1)*(2*n+1)//6


#Method 2
def squareSum1(n):
    s=0
    for i in range(n):
        s=s+i**2
    return s


print(squareSum0(int(input())))

#print(squareSum1(int(input())))
