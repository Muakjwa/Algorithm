import sys
input = sys.stdin.readline

A,B = map(int,input().split())
cnt = 1
while A!=B:
    if A>B:
        print(-1)
        break
    if B%2==0:
        B//=2
        cnt+=1
    elif str(B)[-1]=='1':
        B//=10
        cnt+=1
    else:
        print(-1)
        break
if A==B:
    print(cnt)