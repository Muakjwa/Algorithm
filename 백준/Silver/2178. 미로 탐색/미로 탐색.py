import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int,input().split())
Map = []
cnt = 0
for i in range(N):
    Map.append(list(map(int,input().strip())))
dxy = [(0,1),(1,0),(-1,0),(0,-1)]
q = deque()
q.append((0,0))

while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dxy[i][0]
        nx = x + dxy[i][1]
        if (0<=ny<N and 0<=nx<M):
            if Map[ny][nx]==1:
                q.append((ny,nx))
                Map[ny][nx] = Map[y][x]+1
print(Map[-1][-1])