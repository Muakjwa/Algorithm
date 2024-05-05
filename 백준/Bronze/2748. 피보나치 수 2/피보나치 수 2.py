a=int(input())
lst=[0]*(a+1)
lst[0:3]=[0,1,1]
for i in range(3,a+1):
    lst[i]=lst[i-1]+lst[i-2]
print(lst[a])