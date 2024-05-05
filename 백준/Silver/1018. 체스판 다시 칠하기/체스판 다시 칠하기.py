import sys
N,M = map(int,sys.stdin.readline().strip().split())
chess = []
for _ in range(N):
    chess.append(sys.stdin.readline().strip())
m=65
    
for i in range(N-7):
    for j in range(M-7):
        fwhite=0
        fblack=0
        for k in range(i,i+8):
            for p in range(j,j+8):
                if((k+p)%2==0):
                    if(chess[k][p] == 'B'):
                        fwhite+=1
                    else:
                        fblack+=1
                else:
                    if(chess[k][p] == 'B'):
                        fblack+=1
                    else:
                        fwhite+=1
        m = min(m, fblack, fwhite)
print(m)