var1=input()

def palindrome1(var1):
    var1=var1.lower().split(' ')
    var1=''.join(var1)
    if var1[::-1]==var1:
        print("Yes")
    else:
        print("No")


def palindrome2(var1):
    var2=var1.lower().replace(' ','').replace(",",'').replace('–','').replace("-",'')
    var2=list(var2.strip())
    var2.reverse()
    print("Yes") if ''.join(var2)==var1.lower().replace(" ",'').replace(",",'').replace('–','').replace("-",'') else print("No")

    
palindrome2(var1)