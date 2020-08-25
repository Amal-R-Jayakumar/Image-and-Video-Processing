s1=input("s1 = ")
s2=list(input("s2=").replace(",",'').replace(".",'').replace("'",'').replace('"','').split())
if s1 in s2:
    print("yes")
else:
    print("no")