import sys

N = int(sys.stdin.readline().strip())
building = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    building.append(y)

cnt = 0
stack = []
for build in building:
    if stack == [] and build != 0:
        stack.append(build)
    else:
        while stack != [] and stack[-1] > build:
            stack.pop()
            cnt += 1
        if build == 0:
            continue
        if stack == []:
            stack.append(build)
            continue
        elif stack[-1] == build:
            continue
        elif stack[-1] < build:
            stack.append(build)
            continue

print(cnt + len(stack))