from collections import deque
import sys
n=int(sys.stdin.readline())
que=deque([])

for i in range(n):
    cmd=sys.stdin.readline().split()
    
    if cmd[0]=='push':
        que.append(cmd[1])
    elif cmd[0]=='pop':
        if not que:
            print(-1)
        else:
            print(que.popleft())
    elif cmd[0]=='size':
        print(len(que))
    elif cmd[0]=='empty':
        if not que:
            print(1)
        else:
            print(0)
    elif cmd[0]=='front':
        if not que:
            print(-1)
        else:
            print(que[0])
    elif cmd[0]=='back':
        if not que:
            print(-1)
        else:
            print(que[-1])