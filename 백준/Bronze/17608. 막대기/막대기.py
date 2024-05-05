import sys
input = sys.stdin.readline

N = int(input())
lst = []
mx,cnt = 0,0
for _ in range(N):
    lst.append(int(input()))
while lst:
    p = lst.pop()
    if mx < p:
        mx = p
        cnt+=1
print(cnt)