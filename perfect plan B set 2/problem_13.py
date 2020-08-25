s2=list(input("s = ").replace(",",'').replace(".",'').replace("'",'').replace('"','').split())
for i in s2:
    if len(i)%2==0:
        print(i)