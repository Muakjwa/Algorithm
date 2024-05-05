from collections import deque
m,n,k=map(int,input().split())
lst=[[1]*n for i in range(m)]
count=0
result=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for _ in range(k):
    a1,b1,a2,b2=map(int,input().split())
    for i in range(a1,a2):
        for j in range(b1,b2):
            lst[j][i]=0
def bfs():
    cnt=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and lst[ny][nx]==1:
                lst[ny][nx]=0
                queue.append([nx,ny])
                cnt+=1
    result.append(cnt)
for i in range(m):
    for j in range(n):
        if lst[i][j]==1:
            lst[i][j]=0
            queue=deque([[j,i]])
            bfs()
            count+=1
print(count)
result.sort()
for i in range(len(result)):
    print(result[i], end=' ')