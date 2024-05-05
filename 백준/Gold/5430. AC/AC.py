import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    command = input().rstrip()
    T = int(input())
    array = deque(list(map(str,input().rstrip()[1:-1].split(','))))
    r = 0
    err =0
    if T==0:
        array=[]
    for i in command:
        if i =='R':
            if r==0:
                r=1
            else:
                r=0
        elif len(array)==0:
            err = 1
            break
        else:
            if r==1:
                array.pop()
            else:
                array.popleft()
    if err == 1:
        print('error')
    else:
        if(r==1):
            array.reverse()
        print('['+','.join(array)+']')       