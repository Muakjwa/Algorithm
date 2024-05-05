N, K = map(int,input().split())
coin = []
for i in range(N):
    coin.append(int(input()))
case = [0]*(K+1)
case[0]=1
for i in coin:
    for j in range(i,K+1):
        case[j] += case[j-i]
        
print(case[-1])