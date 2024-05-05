import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
x = int(input())
lst.sort()
start = 0
end = N-1
cnt = 0
while start<end:
    if lst[start]+lst[end]==x:
        cnt+=1
    if lst[start]+lst[end]>=x:
        end-=1
    else:
        start+=1
print(cnt)