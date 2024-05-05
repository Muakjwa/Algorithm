n = int(input())
lst = {}
lst[1]=1
lst[2]=2
lst[3]=4

for i in range(4,11):
    lst[i] = lst[i-1]+lst[i-2]+lst[i-3]
    
for i in range(n):
    print(lst[int(input())])
