List=list(map(str,input("list - ").replace("[",'').replace(",",' ').replace("]",'').replace('"','').replace("'",'').strip().split()))
word=input("word = ")
n=int(input("N = " ))
count=0
for i in range(len(List)):
    print(i,count)
    if List[i]==word:
        count=count+1
        if n==count:
            List.pop(i)
            break
print(f"list - {List}")