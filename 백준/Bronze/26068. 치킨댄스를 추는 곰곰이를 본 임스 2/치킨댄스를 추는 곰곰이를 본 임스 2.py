import sys

N = int(sys.stdin.readline().strip())
canuse = 0

for i in range(N):
    dday = int(sys.stdin.readline().strip().split('-')[1])
    if dday <= 90:
        canuse += 1

print(canuse)