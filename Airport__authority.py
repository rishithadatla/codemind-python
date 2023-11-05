n=int(input())
l=[]
for i in range(0,n):
    m=int(input())
    l.append(m)
target=int(input())
s=0
for i in l:
    if i>target:
        s+=2
    else:
        s+=1
print(s)