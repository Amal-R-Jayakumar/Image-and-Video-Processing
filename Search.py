#Program to search for an element with both linear and binary search at the moment
class Search:
    def __init__(self):
        pass
    def linear_search(self,num,list_of_num):
        for i in list_of_num:
            if num==i: 
                print(f"found at index {list_of_num.index(i)}")
                break
        else:
            print("not found")
    def binary_search(self,num,list_of_num):
        list_of_num.sort()
        print(list_of_num)
        f=0
        l=len(list_of_num)-1
        print(l)
        if num == list_of_num[0]:
            print("Number Found at index 0")
        else:
            while f<=l:
                index=(f+l)//2
                if num > list_of_num[index]:
                    f=index+1
                    print(f,l)
                elif num==list_of_num[index]:
                    print(f"Number Found at index {index}")
                    print(f,l)
                    break
                elif num < list_of_num[index]:
                    l=index-1
                    print(f,l)
            else:
                print("Not found")
                print(f,l)

if __name__== "__main__":
    l=list(map(int,input("Enter the list: ").split()))
    n=int(input("Number to Search: "))
    li=Search()
    li.binary_search(n,l)