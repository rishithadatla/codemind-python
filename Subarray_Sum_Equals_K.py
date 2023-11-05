def subsum(l,k,n):
    result=0
    for i in range(0,n):
        val=0
        for j in range(i,n):
            val+=l[j]
            if val==k:
                result+=1
    return result
n,k=map(int,input().split())
l=list(map(int,input().split()))
m=subsum(l,k,n)
print(m)