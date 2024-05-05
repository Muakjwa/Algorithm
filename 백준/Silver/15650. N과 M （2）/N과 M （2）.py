n,m=map(int,input().split())
arr=[]
visited=[False for i in range(n)]

def back(cnt,k):
    if cnt==m:
        print(*arr)
        return
    for i in range(k,n):
        if visited[i]==True:
            continue
        visited[i]=True
        arr.append(i+1)
        back(cnt+1,i+1)
        visited[i]=False
        arr.pop()
back(0,0)