N = int(input())
D = {}
mx=0
best = ''
for _ in range(N):
    s = input()
    if s in D:
        D[s]+=1
    else:
        D[s]=1
for s in D.keys():
    if mx<D[s]:
        mx=D[s]
        best = [s]
    elif mx==D[s]:
        best.append(s)
print(sorted(best)[0])