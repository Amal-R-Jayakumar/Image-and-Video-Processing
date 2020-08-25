#Method 1
def cubeSum0(n):
    return (n**2)*((n+1)**2)//4


#Method 2
def cubeSum1(n):
    s=0
    for i in range(n):
        s=s+i**3
    return s


print(cubeSum0(int(input())))

#print(cubeSum1(int(input())))

