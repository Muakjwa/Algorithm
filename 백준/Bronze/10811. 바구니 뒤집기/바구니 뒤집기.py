import sys

N, M = map(int, sys.stdin.readline().strip().split())

basket = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    basket = basket[:i-1] + list(reversed(basket[i-1:j])) + basket[j:]

print(' '.join(map(str, basket)))         