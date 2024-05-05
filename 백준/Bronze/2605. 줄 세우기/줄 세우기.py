N = int(input())
num = list(map(int,input().split()))
lst = []
for i in range(N):
    n = num[i]
    lst.insert(i-n,i+1)
print(*lst)