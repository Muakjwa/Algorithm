total = int(input())
num =int(input())
for i in range(num):
    price, cnt = map(int, input().split())
    total -= price*cnt
    
if(total ==0):
    print("Yes")
else:
    print("No")