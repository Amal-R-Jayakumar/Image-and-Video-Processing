import string

var1=input("Enter the string or the number(integer number) you wnat to check: ")
var1=var1.split(' ')
var1=''.join(var1)
if var1[::-1]==var1:
    print("it is a palindrome")
else:
     print("it's not a palindrome")