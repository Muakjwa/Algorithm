n=int(input())
lst=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
visited=[[0]*n for _ in range(n)]
result=[]
for i in range(n):
    lst.append(list(map(int,input())))
    
def dfs(i,j):
    visited[i][j]=1
    global num
    if lst[i][j]==1:
        num+=1
    for k in range(4):
        nx=i+dx[k]
        ny=j+dy[k]
        if 0<=nx<n and 0<=ny<n:
            if visited[nx][ny]==0 and lst[nx][ny]==1:
                dfs(nx,ny)
for i in range(n):
    for j in range(n):
        num=0
        if lst[i][j]==1 and visited[i][j]==0:
            dfs(i,j)
            result.append(num)
            
print(len(result))
for i in sorted(result):
    print(i)