import sys
from collections import deque

S = str(sys.stdin.readline().strip())
T = str(sys.stdin.readline().strip())

q = deque([S])
possible = 0

while True:
    if len(q) == 0:
        break
    s = q.popleft()
    if s == T:
        possible = 1
        break
    sa = s+'A'
    sb = ''.join(reversed(list(s+'B')))
    if sa in T or ''.join(reversed(list(sa))) in T:
        q.append(sa)
    if sb in T or ''.join(reversed(list(sb))) in T:
        q.append(sb)

print(possible)