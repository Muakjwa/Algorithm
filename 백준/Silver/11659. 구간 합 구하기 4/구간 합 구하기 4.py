import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int,input().split()))
for i in range(N-1):
    num[i+1]+=num[i]
    
for _ in range(M):
    i, j = map(int,input().split())
    if i==1:
        print(num[j-1])
    else:
        print(num[j-1]-num[i-2])