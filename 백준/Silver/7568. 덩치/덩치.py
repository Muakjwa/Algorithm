n=int(input())
a=[]
b=[]
e=[1]*n
for i in range(n):
  c,d=map(int,input().split())
  a.append(c)
  b.append(d)
for p in range(n-1):
  for k in range(p+1,n):
    if (a[p]>a[k] and b[p]>b[k]):
      e[k]+=1
    elif (a[p]<a[k] and b[p]<b[k]):
      e[p]+=1
for i in range(n):
  print(e[i],end=" ")