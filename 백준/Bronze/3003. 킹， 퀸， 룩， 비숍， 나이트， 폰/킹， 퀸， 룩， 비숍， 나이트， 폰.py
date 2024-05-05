lst =[1,1,2,2,2,8]
ll = list(map(int,input().split()))
for i in range(len(lst)):
    print(lst[i]-ll[i], end=" ")