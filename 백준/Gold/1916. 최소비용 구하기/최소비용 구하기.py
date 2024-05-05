import sys
input = sys.stdin.readline
INF = 1e9
import heapq

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
A,B = map(int,input().split())
h = [(0,A)]
distance = [INF]*(N+1)
visited = [False]*(N+1)

def dijkstra():
    while h:
        dis, node = heapq.heappop(h)
        if visited[node]==True:
            continue
        visited[node]=True
        distance[node] = min(distance[node],dis)
        for d, c in graph[node]:
            if c+dis<distance[d]:
                heapq.heappush(h,(c+dis,d))
dijkstra()
print(distance[B])