n = int(input())
for _ in range(n):
    lst = list(map(int,input().split()))
    lst.sort(reverse=True)
    print(lst[2])