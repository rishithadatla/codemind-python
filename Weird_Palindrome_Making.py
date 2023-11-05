n=int(input())
for i in range(0,n):
    l=int(input())
    lis=list(map(int,input().split()))
    k=0
    for i in lis:
        k+=i%2
    print(int(k/2))