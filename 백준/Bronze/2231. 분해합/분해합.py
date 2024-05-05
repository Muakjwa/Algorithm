def f(n):
  i=1
  k=[]
  a=n//10
  b=n%10
  k.append(b)
  while a!=0:
    a=a//10
    i+=1
  a=n//10
  for p in range(i-1):
    k.append(a%10)
    a=a//10
  return (n+sum(k))

m=int(input())

for i in range(m):
  if(f(i)==m):
    print(i)
    break
  if(i==m-1):
    print(0)
    break
