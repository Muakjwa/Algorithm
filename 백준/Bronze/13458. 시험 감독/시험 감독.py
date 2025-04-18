import sys
input = sys.stdin.readline

N = int(input().strip())
student = list(map(int, input().strip().split()))
B, C = map(int, input().strip().split())

cnt = 0
for s in student:
    s -= B
    cnt += 1
    if s <= 0:
        continue
    else:
        cnt += (s//C)
        if s%C != 0:
            cnt += 1

print(cnt)