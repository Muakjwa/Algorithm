dx=[0,0,1,-1,-1,1,-1,1]
dy=[-1,1,0,0,-1,-1,1,1]
def bfs(graph,n,m):
    queue=[[n,m]]
    while queue:
        a,b=queue.pop(0)
        for i in range(8):
            nx=b+dx[i]
            ny=a+dy[i]
            if 0<=nx<x and 0<=ny<y and graph[ny][nx]==1:
                graph[ny][nx]=0
                queue.append([ny,nx])
while True:
    x,y=map(int,input().split())
    lst=[]
    count=0
    if x==0and y==0:
        break
    for _ in range(y):
        lst.append(list(map(int,input().split())))
    for m in range(x):
        for n in range(y):
            if lst[n][m]==1:
                lst[n][m]=0
                bfs(lst,n,m)
                count+=1
    print(count)