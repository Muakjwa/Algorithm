import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
num = deque(list(range(1,N+1)))
lst=[]

while len(num)!=1:
    lst.append(num.popleft())
    num.append(num.popleft())
lst.append(num[0])
print(*lst)