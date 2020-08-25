s=input("s = ").split()
s=list(''.join(s).strip())

list2=s.copy()
list2=list(set(list2))
s.sort()
list2.sort()
if s==list2:
    print(True)
else:
    print(False)