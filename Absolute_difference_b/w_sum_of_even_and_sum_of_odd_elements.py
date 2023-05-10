n=int(input())
a=list(map(int,input().split()))
s=0
b=0
for i in a:
    if i%2==0:
        s=s+i
    else:
        b=b+i
print(abs(s-b))