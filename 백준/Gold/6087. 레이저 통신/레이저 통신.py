import sys
from collections import deque
import heapq

W, H = map(int, sys.stdin.readline().strip().split())
MAP = []
point = []
visited = [[[] for _ in range(W)] for _ in range(H)]

for i in range(H):
    row = str(sys.stdin.readline().strip())
    new_row = []
    for j, e in enumerate(row):
        new_row.append(e)
        if e == 'C':
            point.append([i, j])
    MAP.append(new_row)

q = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(4):
    q.append([0, point[0], [point[0][0] + dy[i], point[0][1] + dx[i]]])

def bfs():
    while q:
        mirror, pos, prev_pos = q.popleft()
        y, x = pos
        prev_y, prev_x = prev_pos
        for i in range(4):
            next_y = y + dy[i]
            next_x = x + dx[i]
            if next_y == prev_y and next_x == prev_x:
                continue
            if 0<=next_y<H and 0<=next_x<W:
                if MAP[next_y][next_x] == '*':
                    continue
                new_mirror = mirror
                if next_y - y == y - prev_y and next_x - x == x - prev_x:
                    pass
                else:
                    new_mirror += 1

                if len(visited[next_y][next_x]) != 0 and visited[next_y][next_x][0][0] < new_mirror:
                    continue
                else:
                    if (new_mirror, [y,x]) not in visited[next_y][next_x]:
                        heapq.heappush(visited[next_y][next_x], (new_mirror, [y, x]))
                        q.append([new_mirror, [next_y, next_x], [y, x]])
                        
bfs()
print(visited[point[1][0]][point[1][1]][0][0])