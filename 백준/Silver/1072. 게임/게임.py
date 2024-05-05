X, Y = map(int,input().split())
prob = 100*Y//X
start= 1
end = X

if(prob>=99):
    print(-1)
else:
    while(start<=end):
        mid = (start+end)//2
        if(100*(mid+Y)//(mid+X)!=prob):
            end = mid-1
        else:
            start = mid+1
        
    print(start)