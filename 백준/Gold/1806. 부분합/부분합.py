import sys

N, S = map(int, sys.stdin.readline().strip().split())
lst = list(map(int, sys.stdin.readline().strip().split()))

for i in range(N-1):
    lst[i+1] += lst[i]
lst.insert(0,0)

start = 0
end = 1
shortest_len = 9999999

while start <= N and end <= N:
    if S <= lst[end]-lst[start]:
        if shortest_len > end-start:
            shortest_len = end-start
        start += 1
    else:
        end += 1

if shortest_len == 9999999:
    print(0)
else:
    print(shortest_len)