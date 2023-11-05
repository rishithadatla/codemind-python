n=int(input())
sl=list(map(int,input().split()))
pl=list(map(int,input().split()))
s,p=0,0
s,p=sum(sl),sum(pl)
if s>p:
    print("0")
else:
    print(p-s)