import sys
input = sys.stdin.readline

N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
stack = []
k = 0

def bt():
    if len(stack) == M:
        print(*stack)
        return
    for i in range(len(lst)):
        if lst[i] not in stack:
            stack.append(lst[i])
            bt()
            stack.pop()
bt()