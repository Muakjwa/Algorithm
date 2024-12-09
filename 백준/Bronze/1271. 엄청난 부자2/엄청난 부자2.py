import sys

N, M = map(int, sys.stdin.readline().strip().split())

print(N//M)

print(N%M)