import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]

for j in range(N):
    lst = list(map(int,input().split()))
    i=1
    while lst[i]!=-1:
        graph[lst[0]].append((lst[i],lst[i+1]))
        i+=2
q = deque()
q.append((1,0))
visit = set()
visit.add(1)
mx,pos = 0,0
while q:
    a,c = q.popleft()
    if mx<c:
        mx = c
        pos = a
    for v,d in graph[a]:
        if v not in visit:
            q.append((v,c+d))
            visit.add(v)

q = deque()
q.append((pos,0))
visit = set()
visit.add(pos)
mx,pos = 0,0
while q:
    a,c = q.popleft()
    if mx<c:
        mx = c
        pos = a
    for v,d in graph[a]:
        if v not in visit:
            q.append((v,c+d))
            visit.add(v)
print(mx)