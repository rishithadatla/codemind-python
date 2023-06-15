n=int(input())
l=list(map(int,input().split()))
j=1
gcd=l[0]
while j<n:
    if l[j]%gcd==0:
        j+=1
    else:
      gcd=l[j]%gcd
print(gcd)