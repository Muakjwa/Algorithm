N = int(input())
cnt=0
for _ in range(N):
    stack = []
    s = list(input())
    for i in s:
        if stack and stack[-1]==i:
            stack.pop()
        else:
            stack.append(i)
    if stack==[]:
        cnt+=1
print(cnt)