import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())
D = dict()
for i in range(M+N):
    a,b = map(int,input().split())
    D[a]=b
q= deque()
q.append((1,0))
visited = [0]*101
visited[1]=1
while q:
    n, c = q.popleft()
    if n==100:
        print(c)
        break
    while n in D:
        n = D[n]
    for i in range(1,7):
        if n+i<101 and visited[n+i]==0:
            visited[n+i]=1
            q.append((n+i,c+1))
