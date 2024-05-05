from collections import deque
q = deque()
q.append(1)
N = int(input())
graph=[[] for i in range(N+1)]
for i in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
isin = [0]*(N+1)
tree = [0]*(N+1)

while q:
    v = q.popleft()
    for i in graph[v]:
        if isin[i]==0:
            tree[i]=v
            isin[i]=1
            q.append(i)
for i in range(2,len(tree)):
    print(tree[i])