List=list(map(int,input("list - ").replace("[",'').replace(",",' ').replace("]",'').replace('"','').replace("'",'').strip().split()))
print(List[::-1])
List.reverse()
print(List)