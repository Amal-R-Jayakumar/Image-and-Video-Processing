def primeInterval():
    #Print all prime numbers in an interval.
    lower=int(input("lower: "))
    upper=int(input("upper: "))
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

def checkPrime():
    #Check weather a number is prime or not. 
    num=int(input())
    for i in range(2,num):
        if num%i==0:
            print("not  prime")
            break
    else:
        print("Prime")