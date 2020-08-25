#Method 1
def armstrong1(num):
    temp_1=temp_2=num
    string=list()
    def noOfDigits(temp_1):
        count=0
        while temp_1!=0:
            temp_1=temp_1//10
            count+=1
        return count
    n=noOfDigits(temp_1)
    armstrong=0
    
    while temp_2!=0:
        r=temp_2%10
        temp_2=temp_2//10
        armstrong+=r**n
        string.append("*".join(str(r)*n))
    string.reverse()
    if armstrong==num:
        print(f"Yes\n{num} is an Armstrong number.\n{' + '.join(string)} = {armstrong}")
    else:
        print(f"No\n{num} is not an Armstrong number.\n{' + '.join(string)} = {armstrong}")


#Method 2
def armstrong2(num):
    number=list(num.strip())
    armstrong=0
    for i in number:
        armstrong=armstrong+pow(int(i),len(number))
        number[number.index(i)]="*".join(i*len(number))
#    string.sort()
    print(f"Yes\n{num} is an Armstrong number.\n{' + '.join(number)} = {armstrong}") if armstrong==num else print(f"No\n{num} is not an Armstrong number.\n{' + '.join(number)} = {armstrong}")
    
#armstrong1(int(input()))
armstrong2(input())