import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    x=[]
    for _ in range(N):
        x.append(list(map(int,input().split())))
    x.sort(key = lambda x:x[0])
    m=x[0][1]
    cnt = 1
    for i in range(1,N):
        if m>x[i][1]:
            m = x[i][1]
            cnt+=1
    print(cnt)