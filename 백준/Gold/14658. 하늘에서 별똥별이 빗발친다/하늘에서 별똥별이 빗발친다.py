import sys

N, M, L, K = map(int, sys.stdin.readline().strip().split())

star = []
for _ in range(K):
    x, y = map(int, sys.stdin.readline().strip().split())
    star.append([x,y])

def check_point(x_o, y_o, x, y):
    cnt = 0
    for p_x, p_y in star:
        if x_o <= p_x <= x and y_o <= p_y <= y:
            cnt += 1
    return cnt

result = 0
for x1, y1 in star:
    for x2, y2 in star:
        x = min(x1, x2)
        y = min(y1, y2)

        result = max(result, check_point(x, y, x+L, y+L))

print(K - result)