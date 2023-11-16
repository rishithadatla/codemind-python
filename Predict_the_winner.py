n=int(input())
arr=list(map(int,input().split()))
s,c=0,0
for i in range(0,n):
    if i%2!=0:
        s+=arr[i]
    else:
        c+=arr[i]
a=abs(s-c)
if a%4==0:
    print("X")
else:
    print("Y")