def palin(n):
  rev=str(n)[::-1]
  if int(rev)==n:
     return 0
def reverse(n):
  rev=str(n)[::-1]
  n+=int(rev)
  return n
n=int(input())
n=reverse(n)
while True:
 if palin(n)==0:
    break
 else:
   n=reverse(n)
print(n)