import sys
input = sys.stdin.readline

S = input().rstrip()
result=[]
stack = []
part = False

for s in S:
    if s=='<':
        part = True
        while stack:
            result.append(stack.pop())
    if part==True:
        result.append(s)
    if part == False:
        if s==' ':
            while stack:
                result.append(stack.pop())
            result.append(' ')
        else:
            stack.append(s)
    if s=='>':
        part = False
while stack:
    result.append(stack.pop())
print(''.join(result))