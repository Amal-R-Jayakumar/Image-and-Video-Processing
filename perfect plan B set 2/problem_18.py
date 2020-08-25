def hanoi(n,A,B,C):
    if n==1:
        return C.append(A.pop())
    else:
        hanoi(n-1,A,C,B)
#        print(A,B,C)
        C.append(A.pop())
#        print(A,B,C)
        hanoi(n-1,B,A,C)
#        print(A,B,C)


n=int(input())
A=list(range(n,0,-1))
B=list()
C=list()

hanoi(n,A,B,C)

print(A,B,C)
            


