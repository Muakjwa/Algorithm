import sys
input = sys.stdin.readline
import heapq
N = int(input())
h = []
c = []
mx = 0
for _ in range(N):
    s,t = map(int,input().split())
    heapq.heappush(h, (s,t))
    
while h:
    s,t = heapq.heappop(h)
    if c!= [] and c[0]<=s:
        heapq.heappop(c)
        heapq.heappush(c,t)
    else:
        heapq.heappush(c,t)
    mx = max(mx, len(c))
print(mx)