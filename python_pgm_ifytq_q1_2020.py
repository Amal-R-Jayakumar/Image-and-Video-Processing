import string
old_string=input("Enter Your String here: ")
new_string=old_string.split(" ")
for i in new_string:
    if len(i) <= 2:
        new_string.remove(i)
print(new_string)
new_str=[]
for i in new_string:
    for j in i:
        count=i.count(j)
        if count > 1 :
            new_str.append(i)
print(new_string)
new_str=set(new_str)
print (new_str)
new_str=list(new_str)
for i in new_str:
    for j in new_string:
        if i == j:
            new_string.remove(j)
print(new_string)
if new_string==[]:
    print('-1')
elif len(new_string)==1:
    print(new_string[0])
else:       
    max=len(new_string[0])
    longest_string=''
    for i in new_string:
        if max < len(i):
            longest_string = i
    print(longest_string)
