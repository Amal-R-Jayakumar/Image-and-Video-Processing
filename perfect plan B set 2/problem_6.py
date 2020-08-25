n=list(map(int,input("List = ").replace("[",'').replace(",",' ').replace("]",'').strip().split()))
pos1=int(input("pos1="))
pos2=int(input("pos2="))
def swapPos0(n,pos1,pos2):
    n[pos1-1],n[pos2-1]=n[pos2-1],n[pos1-1]
    print(n)
swapPos0(n,pos1,pos2)
