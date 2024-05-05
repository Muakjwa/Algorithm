a,b,c=map(int,input().split())
k=(c-a)//(a-b)
if (c-a)%(a-b)==0:
  print(k+1)
else:
  print(k+2)