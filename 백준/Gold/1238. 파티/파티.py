import sys
input = sys.stdin.readline
import heapq
INF = 1e9

N,M,X = map(int,input().split())
graph = [[] for _ in range(N+1)]
rgraph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
rvisited = [False]*(N+1)
distance = [INF]*(N+1)
rdistance = [INF]*(N+1)
h = [(0,X)]
g = [(0,X)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    rgraph[b].append((a,c))

def dijkstra():
    while h:
        dis, c = heapq.heappop(h)
        if visited[c]==True:
            continue
        visited[c]=True
        distance[c] = min(distance[c], dis)
        for end, cost in graph[c]:
            if cost+dis < distance[end]:
                heapq.heappush(h,(cost+dis,end))
    while g:
        dis, c = heapq.heappop(g)
        if rvisited[c]==True:
            continue
        rvisited[c]=True
        rdistance[c] = min(rdistance[c], dis)
        for end, cost in rgraph[c]:
            if cost+dis < rdistance[end]:
                heapq.heappush(g,(cost+dis,end))
dijkstra()
d= 0
f =[]
for i in range(N+1):
    f.append(distance[i]+rdistance[i])
for i in range(N+1):
    if f[i]<INF:
        d = max(d,f[i])

print(d)