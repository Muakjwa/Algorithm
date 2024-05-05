import sys
input = sys.stdin.readline
import heapq

N, M, R = map(int,input().split())
item = list(map(int,input().split()))
graph = [[] for _ in range(N+1)]
mx = 0
h = []

for i in range(R):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
def dijkstra():
    s=0
    while(h):
        c, tem, pos = heapq.heappop(h)
        if visited[pos]==False:
            visited[pos]=True
            s+=tem
        for d, dis in graph[pos]:
            if dis + c <= M and visited[d]==False:
                heapq.heappush(h,(c+dis,item[d-1],d))
    return s
                
for i in range(1,N+1):
    visited = [False]*(N+1)
    heapq.heappush(h,(0,item[i-1],i))
    mx = max(mx,dijkstra())
print(mx)