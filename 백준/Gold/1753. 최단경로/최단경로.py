import sys
input = sys.stdin.readline
INF = 1e9
import heapq

V,E = map(int,input().split())
K = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

visited = [False]*(V+1)
distance = [INF]*(V+1)
h = [(0,K)]

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
for i in range(1,len(distance)):
    if distance[i]==INF:
        print('INF')
    else:
        print(distance[i])