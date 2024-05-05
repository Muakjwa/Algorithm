import sys
input = sys.stdin.readline
from collections import deque

q = deque([])
q.append((1, 0))
mx = (1, 0)
N = int(input())
graph = [[] for _ in range(N + 1)]
bgraph = [[] for _ in range(N + 1)]

for i in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    bgraph[b].append((a, c))

while q:
    b, c = q.popleft()
    if mx[1] < c:
        mx = (b, c)
    for v, d in graph[b]:
        q.append((v, c + d))
q.append((mx[0], 0))
visited = [0] * (N + 1)
visited[mx[0]]=1
while q:
    b, c = q.popleft()
    if mx[1] < c:
        mx = (b, c)
    for v, d in graph[b]:
        if visited[v] == 0:
            q.append((v, c + d))
            visited[v] = 1
    for v, d in bgraph[b]:
        if visited[v] == 0:
            q.append((v, c + d))
            visited[v] = 1
print(mx[1])