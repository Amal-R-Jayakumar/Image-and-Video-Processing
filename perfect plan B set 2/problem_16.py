n=list(input().replace("'"," ").replace(",","").replace("{","").replace("}","").replace(":"," ").split())
d=dict()
for i in n:
    if i.isnumeric()==True:
        d[n[n.index(i)-1]]=int(i)
print(sum(d.values()))
