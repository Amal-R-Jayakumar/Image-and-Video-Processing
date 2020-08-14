
def fibinocci(num):
    first=0
    last=1
    list_1=[0,1]
    for _ in range(num):
        newLast=first+last
        first=last
        last=newLast
        list_1.append(newLast)
    list_1.pop()
    return list_1
num=int(input("enter the number of terms: "))
print(fibinocci(num))
print(fibinocci(num)[-1])
