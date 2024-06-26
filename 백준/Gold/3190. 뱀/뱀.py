import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
board = [[0]*N for _ in range(N)]
K = int(input())
for _ in range(K):
    y,x = map(int,input().split())
    board[y-1][x-1]=1
L = int(input())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
direction, cnt, nx, ny = 0, 0, 0, 0
queue = deque()
queue.append((0,0))
dirTo={}
for _ in range(L):
    X,C = input().split()
    dirTo[int(X)]=C

while(True):
    cnt+=1
    nx = nx+dx[direction]
    ny = ny+dy[direction]
    if(nx<0 or nx>=N or ny<0 or ny>=N or ((nx,ny) in queue)):
        break
    else:
        queue.append((nx,ny))
        if(board[ny][nx]==1):
            board[ny][nx]=0
        else:
            queue.popleft()
    if cnt in dirTo:
        C = dirTo[cnt]
        if C == 'D':
            if direction==3:
                direction=0
            else:
                direction+=1
        else:
            if direction ==0:
                direction=3
            else:
                direction-=1
        
print(cnt)