import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())
Map = []
dy = [1,-1,0,0]
dx = [0,0,1,-1]
for _ in range(N):
    Map.append(list(map(int,input().strip())))
def bfs(y,x):
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((y,x,0))
    while q:
        y,x,b = q.popleft()
        if(y==N-1 and x==M-1):
            return visited[y][x][b]+1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<M:
                if Map[ny][nx]==0 and visited[ny][nx][b]==0:
                    q.append((ny,nx,b))
                    visited[ny][nx][b] = visited[y][x][b]+1
                elif Map[ny][nx]==1 and b==0:
                    q.append((ny,nx,b+1))
                    visited[ny][nx][b+1] = visited[y][x][b]+1
    return -1
print(bfs(0,0))
    