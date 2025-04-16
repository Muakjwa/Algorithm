import sys

input = sys.stdin.readline

N, L = map(int, input().strip().split())

MAP = []
for _ in range(N):
    row = list(map(int, input().strip().split()))
    MAP.append(row)

def path_capable(row):
    now = row[0]
    h_prev = now
    idx = 0
    for i, h in enumerate(row):
        if abs(h - now) >= 2:
            return 0
        elif h - now == 0:
            continue
        else:
            if i - idx < L:
                if h_prev != now:
                    if h == h_prev and h-now <0:
                        h_prev = now
                        now = h
                        idx = i
                    else:
                        return 0
                if h - now > 0:
                    return 0
                else:
                    idx = i
                    now = h
            elif h_prev == h and h-now > 0:
                if i - idx < 2*L:
                    return 0
                else:
                    h_prev = now
                    now = h
                    idx = i
            else:
                h_prev = now
                now = h
                idx = i
    if i+1 - idx >= L or now - h_prev > 0:
        return 1
    else:
        return 0

cnt = 0
for row in MAP:
    cnt += path_capable(row)

for i in range(N):
    col = []
    for j in range(N):
        col.append(MAP[j][i])
    cnt += path_capable(col)

print(cnt)