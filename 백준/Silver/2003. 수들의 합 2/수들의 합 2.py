N, M = map(int,input().split())
lst = list(map(int,input().split()))
lst.insert(0,0)

for i in range(1,N+1):
    lst[i] += lst[i-1]
start, end, c = 0,0,0
if lst[end]==M:
    c+=1
while 0<=end<N+1 and 0<=start<N+1:
    if lst[end]-lst[start]==M:
        c+=1
        end+=1
    elif lst[end]-lst[start]<M:
        end+=1
    else:
        start+=1
print(c)