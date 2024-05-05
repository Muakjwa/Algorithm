import sys
from collections import deque
x,y=map(int,sys.stdin.readline().split())
st=list(map(int,sys.stdin.readline().split()))
dq=deque([i for i in range(1,x+1)])
cnt=0
while st:
    if dq.index(st[0])<len(dq)-dq.index(st[0]):
        while st[0]!=dq[0]:
            dq.rotate(-1)
            cnt+=1
        st.pop(0)
        dq.popleft()
    else:
        while st[0]!=dq[0]:
            dq.rotate(1)
            cnt+=1
        st.pop(0)
        dq.popleft()
print(cnt)