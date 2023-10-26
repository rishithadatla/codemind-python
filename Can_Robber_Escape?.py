r=int(input())
l=0
v=list(map(int,input().split()))
for i in range(0,len(v)):
    if v[i]%2!=0:
        l+=1
if l<=2:
    print('YES')
else:
    print('NO')