N = int(input())
value = 1

while(N>0):
    value*=N
    N-=1
cnt=0
val = str(value)
for i in val[::-1]:
    if '0'!=i:
        break
    else:
        cnt+=1
print(cnt)