n=int(input())
for i in range(1,n+1):
    a=int(input())
    b=list(map(int,input().split()))
    d=sorted(b)
    if b==d:
        print('0')
    else:
        print(max(d)-min(d))