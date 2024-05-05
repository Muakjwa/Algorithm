a=int(input())
b=list(input().split())
c=a
for i in range(a):
  if int(b[i])==1:
    c-=1
  else:
    for j in range(2,int(b[i])):
      if int(b[i])%j==0:
        c-=1
        break
print(c)