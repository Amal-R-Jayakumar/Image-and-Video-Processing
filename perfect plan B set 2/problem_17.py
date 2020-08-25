n=input().replace(",",'').replace("'",'').replace("[","").replace("]","").replace("(","").replace(")","").replace('"',"").split()
n1=dict()
for i in n:
    if i.isalpha()==True:
        n1[i]=[int(n[n.index(i)+1])]
print(n1)