N = int(input())
M = int(input())

S = input()

P = 'I'

for i in range(N):
    P = P+'OI'
cnt=0
for i in range(M - len(P)+1):
    if(S[i:i+len(P)] == P):
        cnt+=1
        
print(cnt)