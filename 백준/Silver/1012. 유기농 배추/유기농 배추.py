from collections import deque

def bfs(graph,queue):
    while queue:
        v=queue.popleft()
        for c in range(4):
            nx=v[1]+dx[c]
            ny=v[0]+dy[c]
            if 0<=nx<m and 0<=ny<n and graph[ny][nx]==1:
                queue.append([ny,nx])
                graph[ny][nx]=0
dx=[1,-1,0,0]
dy=[0,0,1,-1]
num=int(input())
for _ in range(num):
    m,n,k=map(int, input().split())
    graph=[[0]*m for i in range(n)]
    count=0
    for _ in range(k):
        i,j=map(int,input().split())
        graph[j][i]=1
    for p in range(n):
        for q in range(m):
            if graph[p][q]==1:
                queue=deque([[p,q]])
                graph[p][q]=0
                bfs(graph,queue)
                count+=1
    print(count)
