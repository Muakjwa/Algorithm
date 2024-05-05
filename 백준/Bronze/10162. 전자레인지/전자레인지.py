D = {300:0,60:0,10:0}
T = int(input())
for i in list(D.keys()):
    D[i] = T//i
    T %= i
    
if(T!=0):
    print(-1)
else:
    print(*list(D.values()))