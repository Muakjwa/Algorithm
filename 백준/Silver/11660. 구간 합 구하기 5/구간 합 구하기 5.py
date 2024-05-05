import sys
input = sys.stdin.readline

N,M = map(int,input().split())
Map = []
for i in range(N):
    Map.append(list(map(int,input().split())))
    for j in range(1,N):
        Map[i][j]+=Map[i][j-1]
    if i>=1:
        for j in range(N):
            Map[i][j] += Map[i-1][j]
        
for _ in range(M):
    y1, x1, y2, x2 = map(int,input().split())
    if x1==1 and y1==1:
        result = Map[y2-1][x2-1]
    elif y1 == 1:
        result = Map[y2-1][x2-1]-Map[y2-1][x1-2]
    elif x1 ==1:
        result = Map[y2-1][x2-1]-Map[y1-2][x2-1]
    else:
        result = Map[y2-1][x2-1]+Map[y1-2][x1-2]-Map[y1-2][x2-1]-Map[y2-1][x1-2]

    print(result)