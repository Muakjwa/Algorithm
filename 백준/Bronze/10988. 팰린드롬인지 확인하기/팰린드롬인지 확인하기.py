S = list(input())
new = []
v =len(S)//2
for i in range(v):
    new.append(S.pop())
    
b = True
for i in range(v):
    if(S[i]!=new[i]):
        b=False
if b:
    print(1)
else:
    print(0)