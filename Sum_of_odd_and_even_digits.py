n=int(input())
arr=list(map(int,input().split()))
s,p=0,0
for i in range(0,n):
    if i%2==0:
        s+=arr[i]
    else:
        p+=arr[i]
if(s-p)==0:
    print("YES")
else:
    print("NO")