N = int(input())
h = list(map(int,input().split()))
cnt = [0]*N
stack = []

stack.append(N-1)
for i in range(N-2,-1,-1):
    while stack and h[stack[-1]]<h[i]:
        cnt[stack.pop()] = i+1
    stack.append(i)
print(*cnt)