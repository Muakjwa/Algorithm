import sys

N = int(sys.stdin.readline().strip())

lst = list(map(int, sys.stdin.readline().strip().split()))

start = 0
end = 0
cnt = 0
S = set()

while True:
    if start >= N:
        break
    elif end >= N and start < N:
        start += 1
        cnt += (end - start)
    elif lst[end] in S:
        S.remove(lst[start])
        start += 1
        cnt += (end - start)
    else:
        cnt += 1
        S.add(lst[end])
        end += 1

print(cnt)