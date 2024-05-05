N = int(input())
S = list(map(int,input().split()))
stack = []
val = [-1]*N

for i in range(N-1):
    stack.append(i)
    while stack and S[stack[-1]]<S[i+1]:
        val[stack.pop()]=S[i+1]
print(*val)