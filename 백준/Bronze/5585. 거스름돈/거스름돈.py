coin = [500,100,50,10,5,1]
cost = 1000-int(input())
cnt=0

for i in coin:
    cnt += cost//i
    cost %= i
    
print(cnt)