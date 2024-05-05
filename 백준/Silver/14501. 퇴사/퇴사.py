N = int(input())
T,P=[],[]

for i in range(N):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)
    
i=N-1
bene=[0]*(N+1)
while(i>=0):
    if(T[i]+i<=N):
        bene[i] = max(bene[i+1], bene[i+T[i]]+P[i])
    else:
        bene[i] = bene[i+1]
    i-=1    
    
print(bene[0])