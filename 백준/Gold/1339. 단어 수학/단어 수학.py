N = int(input())
lst, real = [], []
D, n = {}, {}
it = 9
result = 0
for _ in range(N):
    S = input()
    lst.append(S)
    real.append(S)
for S in lst:
    for i in range(len(S)):
        if S[i] in D:
            D[S[i]]+=(10**(len(S)-i-1))
        else:
            D[S[i]] = (10**(len(S)-i-1))
t = list(D.items())
t.sort(key = lambda x : x[1], reverse=True)
for i in range(len(t)):
    n[t[i][0]]=str(it)
    it-=1

for S in real:
    num = ''
    for s in S:
        num += n[s]
    result += int(num)
print(result)