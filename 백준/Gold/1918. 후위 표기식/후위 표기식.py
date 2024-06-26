import sys
input = sys.stdin.readline

stack = []
result = []
op = ['*','/','+','-']
g = ['(',')']
S = input().strip()
for i in range(len(S)):
    if S[i] not in op and S[i] not in g:
        result.append(S[i])
    else:
        if S[i]=='*' or S[i]=='/':
            while stack:
                if stack[-1]=='*' or stack[-1]=='/':
                    result.append(stack.pop())
                else:
                    break
            stack.append(S[i])
        elif S[i]=='+' or S[i]=='-':
            while stack:
                if stack[-1] in op:
                    result.append(stack.pop())
                else:
                    break
            stack.append(S[i])
        else:
            if S[i]=='(':
                stack.append(S[i])
            else:
                while stack:
                    if stack[-1]=='(':
                        stack.pop()
                        break
                    else:
                        result.append(stack.pop())
while stack:
    result.append(stack.pop())
print(*result,sep='')