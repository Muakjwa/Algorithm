import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().strip().split()))
lst.sort()
diff = 10000000000
one = lst[0]
two = lst[-1]
start = 0
end = N-1
while end>start:
    if abs(lst[start]+lst[end])<diff:
        diff = abs(lst[start]+lst[end])
        one = lst[start]
        two = lst[end]
        if diff ==0:
            break
    if lst[start]+lst[end]>=0:
        end-=1
    else:
        start+=1
print(one,two)