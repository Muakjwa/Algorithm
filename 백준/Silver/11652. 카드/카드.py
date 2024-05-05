N = int(input())
D = {}
mx=0
best = []
for _ in range(N):
    a = int(input())
    if a in D.keys():
        D[a]+=1
    else:
        D[a]=1
for a in D.keys():
    if D[a]>mx:
        mx = D[a]
        best = [a]
    elif D[a]==mx:
        best.append(a)
best.sort()
print(best[0])