N = int(input())

dp = [[0, 0],[0,0],[0,0]]
for i in range(N):
    a,b,c = map(int,input().split())
    dp[0][0], dp[1][0], dp[2][0] = max(dp[0][0],dp[1][0])+a, max(dp[0][0],dp[1][0],dp[2][0])+b, max(dp[1][0],dp[2][0])+c
    dp[0][1], dp[1][1], dp[2][1] = min(dp[0][1],dp[1][1])+a, min(dp[0][1],dp[1][1],dp[2][1])+b, min(dp[1][1],dp[2][1])+c
print(max(dp[0][0], dp[1][0], dp[2][0]),min(dp[0][1], dp[1][1], dp[2][1]))