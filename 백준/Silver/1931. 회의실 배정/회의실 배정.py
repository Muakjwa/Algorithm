N = int(input())
lst=[]
end = 0
cnt=0

for i in range(N):
    a, b = map(int,input().split())
    t = (a,b)
    lst.append(t)
    
lst.sort(key = lambda x : (x[1], x[0]))

for meet in lst:
    if(meet[0]>=end):
        end = meet[1]
        cnt+=1
        
print(cnt)