n,m=map(int,input().split())
b=1
a=n
if m==0:
    print(1)
else:
    for i in range(1,n):
        n*=i
    for i in range(1,a-m+1):
        b*=i
    for i in range(1,m):
        m*=i
    print(int(n/(b*m)))