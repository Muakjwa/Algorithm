N,M = map(int, input().split())
h = list(map(int, input().split()))

l=0
isExist = False
r=max(h)
while(l<=r):
    mid=(l+r)//2
    s= 0
    for i in h:
        if i>mid:
            s += (i-mid)
    if(s>=M):
        l=mid+1
    else:
        r=mid-1
        
print(r)