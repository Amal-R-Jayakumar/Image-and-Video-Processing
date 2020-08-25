List=list(input("str = ").replace(",",' ').replace(".",'').replace('"','').replace("'",'').split())
#print(f'\nstr = "{" ".join(List[::-1])}"')

for i in range(len(List)//2):
    List[i],List[0-i-1]=List[0-i-1],List[i]

#List.reverse()
print(f'str = "{" ".join(List)}"')