import sys
import heapq

N, M = map(int, sys.stdin.readline().strip().split())

Distance = [99999999 for _ in range(N+1)]
Cow = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().strip().split())

    Cow[A].append((B,C))
    Cow[B].append((A,C))


q = [(0, 1)]
while len(q):
    cow, pos = heapq.heappop(q)
    for next_pos, next_cow in Cow[pos]:
        new_cow = cow + next_cow
        if new_cow < Distance[next_pos]:
            Distance[next_pos] = new_cow
            heapq.heappush(q, (new_cow, next_pos))

print(Distance[N])