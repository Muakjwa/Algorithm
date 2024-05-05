import sys
input = sys.stdin.readline

N = int(input())
path = []
for _ in range(N):
    path.append(list(map(int,input().split())))
    
ispath = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if(path[j][k]==1):
                ispath[j][k]=1
            elif((path[j][i]==1 or ispath[j][i]==1) and (path[i][k]==1 or ispath[i][k])):
                ispath[j][k]=1
for i in range(N):
    for j in range(N):
        print(ispath[i][j],end=' ')
    print()