N = int(input())
i=1
cnt=0
while(True):
    if N==0:
        break
    if N==i:
        cnt+=1
        N-=i
        break
    elif N>=2*i+1:
        cnt+=1
        N-=i
    i+=1
print(cnt)