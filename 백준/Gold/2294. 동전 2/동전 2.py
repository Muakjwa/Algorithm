import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coin = []
case = [10001]*(k+1)
case[0] = 0
for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse = True)
for i in coin:
    for j in range(len(case)):
        if i<=j:
            case[j] = min(case[j], case[j-i]+1)
if case[k]==10001:
    print(-1)
else:
    print(case[k])