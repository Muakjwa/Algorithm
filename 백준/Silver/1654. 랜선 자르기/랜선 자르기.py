K, N = map(int , input().split())
lan = []
for i in range(K):
    lan.append(int(input()))

l, r = 1, max(lan)

while(l<=r):
    mid = (l+r)//2
    cnt=0
    for line in lan:
        cnt += (line//mid)
    if(cnt>=N):
        l = mid+1
    else:
        r = mid-1
        
print(r)