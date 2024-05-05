import sys
input = sys.stdin.readline
import heapq

N,K = map(int,input().split())
jewel, price, Bag = [], [], []
result = 0
for _ in range(N):
    M,V = map(int,input().split())
    heapq.heappush(jewel,(M,V))
for _ in range(K):
    Bag.append(int(input()))
Bag.sort()
for size in Bag:
    while jewel!=[] and size>=jewel[0][0]:
        m,v = heapq.heappop(jewel)
        heapq.heappush(price,-v)
    if price!=[]:
        result += -1*heapq.heappop(price)
print(result)