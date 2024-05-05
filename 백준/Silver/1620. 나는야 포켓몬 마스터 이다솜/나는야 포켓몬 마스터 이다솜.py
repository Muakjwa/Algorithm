import sys

N, M = map(int, sys.stdin.readline().split())
name = {}
num = {}

for i in range(N):
    num[i+1] = sys.stdin.readline().rstrip()
    name[num[i+1]] = i+1
    
for i in range(M):
    got = sys.stdin.readline().rstrip()
    if got.isdigit():
        print(num[int(got)])
    else:
        print(name[got])