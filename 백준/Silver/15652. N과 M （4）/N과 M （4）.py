n,m=map(int,input().split())
arr=[]

def back(cnt,k):
    if (cnt==m):
        print(*arr)
        return
    for i in range(k,n):
        arr.append(i+1)
        back(cnt+1,i)
        arr.pop()
back(0,0)