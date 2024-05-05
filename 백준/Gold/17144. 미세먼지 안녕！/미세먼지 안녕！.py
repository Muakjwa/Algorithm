import sys
input = sys.stdin.readline

R,C,T = map(int,input().split())
lst = []
aircon = []
dy, dx =[0,0,1,-1], [1,-1,0,0]
fdy, fdx = [0,-1,0,1], [1,0,-1,0]
sdy, sdx = [0,1,0,-1], [1,0,-1,0]
S=0

for i in range(R):
    l = list(map(int,input().split()))
    if -1 in l:
        aircon.append([i,l.index(-1)])
    lst.append(l)
    
    
def diff():
    p = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if lst[i][j]>4:
                cnt=0
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if 0<=ny<R and 0<=nx<C and lst[ny][nx]!=-1:
                        cnt += 1
                        p[ny][nx]+=lst[i][j]//5
                lst[i][j] -= cnt*(lst[i][j]//5)
    for i in range(R):
        for j in range(C):
            lst[i][j] += p[i][j]

def air():
    fy, fx, sy, sx = aircon[0][0], aircon[0][1], aircon[1][0], aircon[1][1]
    ny, nx = fy, fx+1
    ftemp = 0
    for i in range(4):
        while True:
            ny = fy + fdy[i]
            nx = fx + fdx[i]
            if 0<=ny<R and 0<=nx<C:
                if lst[ny][nx]==-1:
                    break
                temp = lst[ny][nx]
                lst[ny][nx] = ftemp
                ftemp = temp
                fy, fx = ny, nx
            else:
                break
    ny, nx = sy, sx+1
    ftemp = 0
    for i in range(4):
        while True:
            ny = sy + sdy[i]
            nx = sx + sdx[i]
            if 0<=ny<R and 0<=nx<C:
                if lst[ny][nx]==-1:
                    break
                temp = lst[ny][nx]
                lst[ny][nx] = ftemp
                ftemp = temp
                sy, sx = ny, nx
            else:
                break
                
for i in range(T):
    diff()
    air()
    
for i in range(R):
    S+= sum(lst[i])
print(S+2)