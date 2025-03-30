import sys
import heapq

cnt = 0
while True:
    cnt += 1
    N = int(sys.stdin.readline().strip())
    if N == 0 :
        break

    Map = []
    for _ in range(N):
        row = list(map(int, sys.stdin.readline().strip().split()))
        Map.append(row)

    log = [[9999999] * N for _ in range(N)]
    q = []
    heapq.heappush(q, (Map[0][0],0,0))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while len(q):
        cost, x, y = heapq.heappop(q)
        if x == N-1 and y == N-1:
            print(f"Problem {cnt}: {cost}")
            break

        for i in range(4):
            if dx[i]+x >= 0 and dx[i]+x < N and dy[i]+y >= 0 and dy[i]+y < N:
                if cost + Map[dx[i]+x][dy[i]+y] < log[dx[i]+x][dy[i]+y]:
                    log[dx[i]+x][dy[i]+y] = cost + Map[dx[i]+x][dy[i]+y]
                    heapq.heappush(q, (cost+Map[dx[i]+x][dy[i]+y], dx[i]+x, dy[i]+y))