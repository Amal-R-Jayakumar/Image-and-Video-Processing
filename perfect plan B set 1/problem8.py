#Python program to check whether a number is Prime or not
#Method 1
def checkPrime0(n):
    if n<=1:
        print("false")
    for i in range(2 , n//2+1):
        if n % i == 0:
            print("false")
            break
    else:
        print("true")

#Method 2
def checkPrime1(num):
    k=1
    p1=2
    p2=3
    while p1 < num and p2 < num:
        if num % p1==0 or num % p2==0:
            print("false")
            break
        p1=6*k-1
        p2=6*k+1
        k+=1
    else:
        print("true")


checkPrime1(int(input("n = ")))