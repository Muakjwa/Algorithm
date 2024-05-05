import sys

N = int(input())
M = int(input())
broken = list(map(int,sys.stdin.readline().split()))
Min = abs(100-N)

for i in range(1000001):
    for j in range(len(str(i))):
        if int(str(i)[j]) in broken:
            break
        elif j == len(str(i))-1:
            Min = min(Min, abs(i-N)+len(str(i)))
print(Min)
    