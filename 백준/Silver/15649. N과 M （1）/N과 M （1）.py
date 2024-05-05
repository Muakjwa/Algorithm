n,m=map(int,input().split())
arr=[]
visited=[False for i in range(n)]


def back(cnt):
    if(cnt==m):
        print(*arr)
        return
    for i in range(n):
        if visited[i]==True:
            continue
        visited[i]=True
        arr.append(i+1)
        back(cnt+1)
        arr.pop()
        visited[i]=False
back(0)
        