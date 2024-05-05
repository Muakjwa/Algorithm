from collections import deque
x,y=map(int,input().split())
dx=[1,-1,0,0]
dy=[0,0,1,-1]
queue=deque()
graph=[]
for _ in range(y):
    graph.append(list(map(int,input().split())))
def bfs():
    while queue:
        a,b=queue.popleft()
        for i in range(4):
            nx=b+dx[i]
            ny=a+dy[i]
            if 0<=nx<x and 0<=ny<y and graph[ny][nx]==0:
                graph[ny][nx]=graph[a][b]+1
                queue.append([ny,nx])
for i in range(y):
    for j in range(x):
        if graph[i][j]==1:
            queue.append([i,j])
bfs()
isTrue=False
result=-2
for i in graph:
    for j in i:
        if j==0:
            isTrue=True
        result=max(result,j)
if isTrue==True:
    print(-1)
elif result==1:
    print(0)
else:
    print(result-1)