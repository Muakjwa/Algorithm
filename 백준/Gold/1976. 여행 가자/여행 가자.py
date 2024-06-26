N = int(input())
M = int(input())
parent = [i for i in range(N+1)]

def find_parent(node):
    if node!=parent[node]:
        parent[node] = find_parent(parent[node])
    return parent[node]

for i in range(N):
    lst = list(map(int,input().split()))
    for j in range(len(lst)):
        if lst[j]==1:
            a = find_parent(i+1)
            b = find_parent(j+1)
            if a==b:
                continue
            elif a>b:
                parent[a] = b
            else:
                parent[b] = a
travel = list(map(int,input().split()))
p = find_parent(travel[0])
avail = True
for i in range(1,len(travel)):
    if p != find_parent(travel[i]):
        avail = False
if avail==True:
    print("YES")
else:
    print("NO")