import math

def area1(r):
    print(f"Area: {(22/7)*(r**2)}")
def area2(r):
    print(f"Area: {math.pi*r**2}")

area1(int(input("Radius: ")))
#area2(int(input("Radius: ")))