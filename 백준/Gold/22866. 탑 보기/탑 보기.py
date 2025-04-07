import sys

N = int(sys.stdin.readline().strip())

building = list(map(int, sys.stdin.readline().strip().split()))

stack = []
cnt = []

for i, h in enumerate(building):
    while stack != [] and stack[-1][0] <= h:
        stack.pop()

    if stack != []:
        cnt.append([len(stack), stack[-1][1]])
    else:
        cnt.append([0, 900000])
    stack.append((h, i+1))

building.reverse()
stack = []

for i, h in enumerate(building):
    while stack != [] and stack[-1][0] <= h:
        stack.pop()
    if stack != []:
        cnt[N-i-1][0] += len(stack)
        if abs(N-i - cnt[N-i-1][1]) > abs(stack[-1][1]- N + i):
            cnt[N-i-1][1] = stack[-1][1]
    stack.append((h, N - i))

for c, i in cnt:
    if c == 0:
        print(0)
    else:
        print(c, i)