import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int,input().split())
lst = []
parent = [i for i in range(N+1)]

def find_parent(node):
    if node != parent[node]:
        parent[node] = find_parent(parent[node])
    return parent[node]
for _ in range(M):
    c, a, b = map(int,input().split())
    if c == 1:
        if find_parent(a)==find_parent(b):
            print("YES")
        else:
            print("NO")
    elif c==0:
        s1 = find_parent(a)
        s2 = find_parent(b)
        if s1 == s2:
            continue
        elif s1>s2:
            parent[s1] = s2
        else:
            parent[s2] = s1