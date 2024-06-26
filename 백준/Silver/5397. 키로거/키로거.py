import sys
input = sys.stdin.readline

N= int(input())
for _ in range(N):
    S = input().rstrip()
    left = []
    right = []
    for i in S:
        if i =='<':
            if left!=[]:
                right.append(left.pop())
        elif i=='>':
            if right != []:
                left.append(right.pop())
        elif i=='-':
            if left != []:
                left.pop()
        else:
            left.append(i)
    while right:
        left.append(right.pop())
    print(''.join(left))