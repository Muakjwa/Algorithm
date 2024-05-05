import heapq
import sys
N = int(input())
heap=[]
for _ in range(N):
    T = int(sys.stdin.readline())
    if(T==0):
        if(len(heap)==0):
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(abs(T),T))
        