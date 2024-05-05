S = input()
S = S.strip(S[0])
cnt = 0
while S:
    f = S[0]
    cnt+=1
    S = S.strip(f)
print(cnt)