n=int(input())
a=[0 for i in range(301)]
for i in range(n):
    a[i]=int(input())
b=[0 for i in range(301)]
b[0]=a[0]
b[1]=a[0]+a[1]
b[2]=max(a[0]+a[2],a[1]+a[2])
for i in range(3,n):
    b[i]=max(b[i-3]+a[i-1]+a[i],b[i-2]+a[i])
print(b[n-1])