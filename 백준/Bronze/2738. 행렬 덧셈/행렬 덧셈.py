N, M = map(int,input().split())

tlst = [[0 for _ in range(M)] for _ in range(N)]
flst = []
slst = []
for i in range(N):
    flst.append(list(map(int,input().split())))
    
for i in range(N):
    slst.append(list(map(int,input().split())))
    
for i in range(N):
    for j in range(M):
        tlst[i][j] = flst[i][j]+slst[i][j]
        
for i in range(N):
    for j in range(M):
        print(tlst[i][j],end=" ")
    print()