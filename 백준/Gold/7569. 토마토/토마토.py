from collections import deque

M, N, H = map(int,input().split())
tomato = []

for _ in range(H):
    plane = []
    for _ in range(N):
        plane.append(list(map(int,input().split())))
    tomato.append(plane)
    
dxyz = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
cnt=0
position = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if(tomato[i][j][k]==1):
                position.append([k,j,i])

while(len(position)!=0):
    cnt+=1
    for i in range(len(position)):
        val = position.popleft()
        for j in range(6):
            dx = val[0]+dxyz[j][0]; dy = val[1]+dxyz[j][1]; dz = val[2]+dxyz[j][2]
            if(0<=dx<M and 0<=dy<N and 0<=dz<H):
                if(tomato[dz][dy][dx]==0):
                    position.append([dx,dy,dz])
                    tomato[dz][dy][dx] = 1
cnt-=1
for i in range(H):
    for j in range(N):
        for k in range(M):
            if(tomato[i][j][k]==0):
                cnt = -1                           
                            
print(cnt)