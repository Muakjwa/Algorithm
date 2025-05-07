import sys

N, M = map(int, sys.stdin.readline().strip().split())

A = [0] + list(map(int, sys.stdin.readline().strip().split()))
C = [0] + list(map(int, sys.stdin.readline().strip().split()))

bag = [[0] * (N+1) for _ in range(10001)]

for i in range(1, N+1):
    if C[i] == 0:
        bag[0][i] = max(bag[0]) + A[i]
    for j in range(1, 10001):
        if C[i] <= j:
            bag[j][i] = max(bag[j][i-1], bag[j-C[i]][i-1] + A[i])
        else:
            bag[j][i] = bag[j][i-1]

def result():
    for i in range(0, 10001):
        for j in range(1, N+1):
            if bag[i][j] >= M:
                return i

print(result())