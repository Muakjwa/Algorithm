import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
Map = []
start = (0, 0)

for i in range(N):
    row = list(map(int, sys.stdin.readline().strip().split()))
    for j, element in enumerate(row):
        if element == 2:
            start = (i, j)
    Map.append(row)

visited = [[-1] * M for _ in range(N)]
q = deque([(start[0], start[1])])
visited[start[0]][start[1]] = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    y, x = q.popleft()
    for i in range(4):
        if 0<= y+dy[i] <N and 0<= x+dx[i] <M:
            if visited[y+dy[i]][x+dx[i]] == -1:
                if Map[y+dy[i]][x+dx[i]] != 0:
                    visited[y+dy[i]][x+dx[i]] = visited[y][x]+1
                    q.append((y+dy[i], x+dx[i]))
                else:
                    visited[y+dy[i]][x+dx[i]] = 0

for i, row in enumerate(visited):
    for j, e in enumerate(row):
        if Map[i][j] == 0:
            print(0, end = ' ')
        else:
            print(e, end = ' ')
    print()