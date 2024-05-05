N = int(input())
d = list(map(int,input().split()))
cost = list(map(int,input().split()))
cost.pop()
total_cost, M = 0, 1000000001

for i in range(N-1):
    M = min(M,cost[i])
    total_cost+=M*d[i]
print(total_cost)