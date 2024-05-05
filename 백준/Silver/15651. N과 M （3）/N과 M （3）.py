n,m=map(int,input().split())
arr=[]
def back(cnt):
    if cnt==m:
        print(*arr)
        return
    for i in range(n):
        arr.append(i+1)
        back(cnt+1)
        arr.pop()
back(0)