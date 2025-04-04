import sys

N = int(sys.stdin.readline().strip())

building = list(map(int, sys.stdin.readline().strip().split()))

maximum = 0

def counting(idx):
    dPlus = -1e9
    dMinus = -1e9
    idxPlus = idx + 1
    idxMinus = idx - 1
    cnt = 0

    while idxPlus < N:
        dx = (building[idxPlus] - building[idx])/(idxPlus - idx)
        if dPlus < dx:
            dPlus = dx
            cnt += 1
        idxPlus += 1

    while idxMinus >= 0:
        dx = (building[idxMinus] - building[idx])/(idx - idxMinus)
        if dMinus < dx:
            dMinus = dx
            cnt += 1
        idxMinus -= 1

    return cnt

for i in range(N):
    maximum = max(maximum, counting(i))

print(maximum)