import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()
print(round(sum(lst)/len(lst)))
print(lst[N//2])
x = Counter(lst).most_common()
if len(x)>=2 and x[0][1]==x[1][1]:
    s = x[1][0]
else:
    s = x[0][0]
print(s)
print(max(lst)-min(lst))