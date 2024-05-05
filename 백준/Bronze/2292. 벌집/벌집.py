n=int(input())
b=1
for i in range(n):
  a=b
  b+=6*i
  if (n==1):
    print(1)
    break
  elif (a<n<=b):
    print(i+1)
    break