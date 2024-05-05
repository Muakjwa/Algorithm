n=int(input())
lst=[]
result=[]
p=0
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def bfs(x,y):
    while queue:
        a,b=queue.pop(0)
        for i in range(4):
            nx=b+dx[i]
            ny=a+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[ny][nx]==1:
                queue.append([ny,nx])
                graph[ny][nx]=0

for _ in range(n):
    a=list(map(int,input().split()))
    lst.append(a)
    p=max(p,max(a))
for k in range(0,101):
    graph=[[1]*n for i in range(n)]
    count=0
    for i in range(n):
        for j in range(n):
            if lst[i][j]<=k:
                graph[i][j]=0
    for i in range(n):
        for j in range(n):
            if graph[i][j]==1:
                graph[i][j]=0
                queue=[[i,j]]
                bfs(i,j)
                count+=1
    result.append(count)
print(max(result))