import sys

H, W = map(int, sys.stdin.readline().strip().split())

world = list(map(int,sys.stdin.readline().strip().split()))

floor = []

for i in range(H+1):
    cnt = []
    for j, flr in enumerate(world):
        if flr > i:
            cnt.append(j)
    floor.append(cnt)

rain_drop = 0
for cnt in floor:
    if cnt != []:
        if len(cnt) >= 2:
            diff = max(cnt) - min(cnt) + 1 - len(cnt)
            rain_drop += diff

print(rain_drop)