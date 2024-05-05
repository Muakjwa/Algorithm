M,N = map(int,input().split())
map_ = []
dp = [[-1 for _ in range(N)] for _ in range(M)]
dx, dy =[1, -1, 0, 0], [0, 0, 1, -1]
cnt = 0

for _ in range(M):
    map_.append(list(map(int,input().split())))
    
def down(m, n):
    if(m==M-1 and n==N-1):
        return 1
    if(dp[m][n]!=-1):
        return dp[m][n]
       
    ways=0
    for i in range(4):
        if(0<=m+dy[i]<M and 0<=n+dx[i]<N):
            if(map_[m+dy[i]][n+dx[i]]<map_[m][n]):
                ways += down(m+dy[i],n+dx[i])
            
    dp[m][n] = ways
    return dp[m][n]
    
    
print(down(0,0))