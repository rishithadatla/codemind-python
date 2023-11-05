def subarray(l,r):
    result=0
    for i in range(l,r+1):
        val=0
        for j in range(i,r+1):
            val+=j
            if val%2!=0:
                result+=1
    return result
l=int(input())
r=int(input())
m=subarray(l,r)
print(m)