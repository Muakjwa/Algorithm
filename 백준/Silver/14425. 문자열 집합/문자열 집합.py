N, M = map(int,input().split())
s = set()
cnt=0
for _ in range(N):
    s.add(input())
for _ in range(M):
    S = input()
    if S in s:
        cnt+=1
    
print(cnt)