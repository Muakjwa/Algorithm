import sys
input = sys.stdin.readline
from collections import deque

dx = [2,2,-2,-2,1,1,-1,-1]
dy = [1,-1,1,-1,2,-2,2,-2]

def bfs(y,x,c):
    q = deque()
    q.append((y,x,c))
    visited = set()
    while q:
        y,x,c = q.popleft()
        visited.add((y,x))
        if y==ty and x==tx:
            return c
            break
        for i in range(8):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<I and 0<=nx<I and (ny,nx) not in visited:
                q.append((ny,nx,c+1))
                visited.add((ny,nx))

T = int(input())
for _ in range(T):
    I = int(input())
    y,x = map(int,input().strip().split())
    ty, tx = map(int,input().strip().split())
    print(bfs(y,x,0))