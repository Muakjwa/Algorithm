N, M = map(int,input().split())
r,c,d=map(int,input().split())
di = [(0,-1),(1,0),(0,1),(-1,0)]
Map = []
clean = [[0]*M for _ in range(N)]
cnt = 0
for _ in range(N):
    Map.append(list(map(int,input().split())))

while True:
    if clean[r][c]==0:
        cnt+=1
        clean[r][c]=1
    if ((clean[r][c+1]==1 or Map[r][c+1]==1) and (clean[r][c-1]==1 or Map[r][c-1]==1)
        and (clean[r+1][c]==1 or Map[r+1][c]==1) and (clean[r-1][c]==1 or Map[r-1][c]==1)):
        if Map[r+di[(d+2)%4][1]][c+di[(d+2)%4][0]]==1:
            break
        else:
            r+=di[(d+2)%4][1]
            c+=di[(d+2)%4][0]
    else:
        if d==0:
            d=3
        else:
            d-=1
        if Map[r+di[d][1]][c+di[d][0]]==0 and clean[r+di[d][1]][c+di[d][0]]==0:
            r+=di[d][1]
            c+=di[d][0]
            
            
print(cnt)