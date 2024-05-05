import sys
input =sys.stdin.readline
import heapq

N,M = map(int,input().split())
I = [0]*(N+1)
D = [[] for _ in range(N+1)]
h = []

for _ in range(M):
    a,b = map(int,input().split())
    I[b] +=1
    D[a].append(b)
for i in range(1,N+1):
    if I[i]==0:
        heapq.heappush(h,i)
while h:
    v = heapq.heappop(h)
    print(v,end=' ')
    for i in D[v]:
        I[i]-=1
        if I[i]==0:
            heapq.heappush(h,i)
            