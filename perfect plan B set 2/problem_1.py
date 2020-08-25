list_1=list(map(int,input().strip().split()))
def swap(swapList):
    temp=swapList[0]
    swapList[0]=swapList[-1]
    swapList[-1]=temp
    return(swapList)
#print(swap(list_1))



def swap1(list_1):
    list_1[0],list_1[-1]=list_1[-1],list_1[0]
    return list_1
#print(swap1(list_1))


def swap2(list_1):
    var1=list_1.pop(0)
    var2=list_1.pop(-1)
    list_1.append(var1)
    list_1.insert(0,var2)
    return list_1
print(swap2(list_1))
