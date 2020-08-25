import math

#Method - 1
def fact1(num):
    return math.factorial(num)

#Method - 2: Pass in the number when called
def fact2(num):
    p=1
    for i in range(1,num+1):
        p=p*i
    print(p)

#Method - 3: Reccursion
def fact3(num):
    if num==0:
        return 1
    return (num*fact3(num-1))

print(fact1(int(input("Number: "))))

fact2(int(input("Number: ")))

print(fact3(int(input("Number: "))))
