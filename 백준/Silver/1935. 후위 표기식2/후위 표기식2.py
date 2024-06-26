import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()
stack = []
D = {}
for i in range(N):
    a= int(input())
    D[chr(65+i)]=a

for i in S:
    if i=='*' or i=='+' or i=='-' or i=='/':
        a = stack.pop()
        b = stack.pop()
        if i=='*':
            stack.append(a*b)
        elif i=='/':
            stack.append(b/a)
        elif i=='+':
            stack.append(a+b)
        else:
            stack.append(b-a)
    else:
        stack.append(D[i])
print('{0:.2f}'.format(stack.pop()))
