M = int(input())
N = int(input())

k=1
m = 10001
s = 0

while(k**2 <= N):
    if(k**2>=M):
        s+=(k**2)
        m = min(m, k**2)
    k+=1

if(s==0):
    print(-1)
else:
    print(s)
    print(m)