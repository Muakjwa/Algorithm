import sys
sys.setrecursionlimit(1000000)

N=int(input())
color = []
dxy = [[1,0],[-1,0],[0,1],[0,-1]]

for i in range(N):
    color.append(list(input()))
    
def bfs(x,y):
    num[y][x]=1
    c = color[y][x]
    for i in range(4):
        dx = dxy[i][0] + x
        dy = dxy[i][1] + y
        if(0<=dx<N and 0<=dy<N):
            if(color[dy][dx]==c and num[dy][dx]==0):
                bfs(dx,dy)
num = [[0 for _ in range(N)] for _ in range(N)]
normal_cnt = 0
abnormal_cnt = 0
for i in range(N):
    for j in range(N):
        if(num[i][j] == 0):
            bfs(j,i)
            normal_cnt+=1
            
for i in range(N):
    for j in range(N):
        if(color[i][j]=='G'):
            color[i][j]='R'

num = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if(num[i][j] == 0):
            bfs(j,i)
            abnormal_cnt+=1
            
print(normal_cnt, abnormal_cnt)