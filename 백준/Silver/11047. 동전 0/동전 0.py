lst=[]
count=0
n,m=map(int,input().split())
for i in range(n):
    lst.append(int(input()))
lst.reverse()
for coin in lst:
    count+=m//coin
    m%=coin
print(count)