import sys
input = sys.stdin.readline

N = int(input())

S = list(map(int,input().split()))
dp = [0]*N
dp[0] = 1

for i in range(1,N):
    dp[i]=1
    for j in range(i):
        if S[i]>S[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
k = max(dp)
result = []
for i in range(N-1,-1,-1):
    if k == dp[i]:
        result.append(S[i])
        k-=1
result.reverse()
print(*result)