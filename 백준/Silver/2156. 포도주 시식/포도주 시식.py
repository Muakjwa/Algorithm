N = int(input())
wine = []

for i in range(N):
    wine.append(int(input()))
    
dp = [0]*N
dp[0] = wine[0]
if N==1:
    print(dp[0])
else:
    dp[1] = wine[0]+wine[1]
    if N==2:
        print(dp[1])
    else:
        dp[2] = max(wine[0]+wine[2], dp[1], wine[1]+wine[2])

        for i in range(3,N):
            dp[i] = max(dp[i-1], dp[i-2]+wine[i], dp[i-3]+wine[i]+wine[i-1])
    
        print(dp[-1])