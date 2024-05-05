N = int(input())
isExist=False
cnt=0
while(N>=0):
    if(N==0):
        print(cnt)
        isExist=True
        break
    elif(N%5==0):
        print(cnt+N//5)
        isExist=True
        break
    else:
        N-=3
        cnt+=1
        
if(isExist==False):
    print(-1)