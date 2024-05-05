import sys
input = sys.stdin.readline

N,M = map(int,input().split())
lst = list(set(list(map(int,input().split()))))
lst.sort()
stack = []

def bt(k):
    if len(stack)==M:
        print(*stack)
        return
    for i in range(k,len(lst)):
        stack.append(lst[i])
        bt(i)
        stack.pop()
        
bt(0)