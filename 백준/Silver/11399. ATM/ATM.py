import sys
N = int(input())
time = list(map(int,sys.stdin.readline().strip().split()))

time.sort(reverse=True)
value=0

for i in range(len(time)):
    value+=(time[i]*(i+1))
    
print(value)