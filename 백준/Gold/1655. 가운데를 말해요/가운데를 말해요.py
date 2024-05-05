import sys
input = sys.stdin.readline
import heapq

N = int(input())
left = []
right = []
for i in range(N):
    a = int(input())
    heapq.heappush(right,a)
    if len(right)>len(left)+1:
        heapq.heappush(left,-1*heapq.heappop(right))
    while True:
        if left!= [] and right != [] and -1*left[0]>right[0]:
            heapq.heappush(right,-1*heapq.heappop(left))
            heapq.heappush(left,-1*heapq.heappop(right))
        else:
            break
    if len(right) == len(left):
        if right[0]> -left[0]:
            print(-left[0])
        else:
            print(right[0])
    else:
        print(right[0])