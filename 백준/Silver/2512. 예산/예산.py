N = int(input())
money = list(map(int, input().split()))
    
M = int(input())

start, end = 0,max(money)
while(start<=end):
    mid = (start+end)//2
    pred = 0
    for i in range(N):
        if(money[i]>mid):
            pred+=mid
        else:
            pred+=money[i]
    if(pred>M):
        end = mid-1
    else:
        start = mid+1
        
print(min(end , max(money)))