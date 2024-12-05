import sys

N, M = map(int, sys.stdin.readline().strip().split())

basket = [0] * N

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().strip().split())

    for num in range(i-1, j):
        basket[num] = k

for number in basket:
    print(number, end=" ")