import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a,b = map(int,input().split())
    lst = [a**1%10, a**2%10, a**3%10, a**4%10]
    if lst[(b-1)%4]==0:
        print(10)
    else:
        print(lst[(b-1)%4])