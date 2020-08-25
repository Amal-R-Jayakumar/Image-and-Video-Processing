import math

#compound interest(considering it's compounded monthly(n=12), weekly(n=54) or daily(n=365))

def CI():
    p,t,r,n=int(input("Principle  (amount): ")),float(input("Time: ")),float(input("Rate: ")),int(input("How many times interest is recieved: "))
    print(f"Compound Interest = {p*pow(1+r/(n*100),(n*t))-p}")
#compound interest(considering it's compounded annually)

def annualCI():
    p,t,r=int(input("Principle  (amount): ")),float(input("Time: ")),float(input("Rate/year in percentage: "))
    print(f"Compound Interest = {p*((1+r/(100))**(t))}")

#continous compound interest
def contCI():
    p,t,r=int(input("Principle  (amount): ")),float(input("Time: ")),float(input("Rate: "))
    ci = p*(math.e**(r*t))
    print(f"Compound Interest = {ci}")

#remove the hash to call CI with n

#CI()

#contCI

annualCI()
