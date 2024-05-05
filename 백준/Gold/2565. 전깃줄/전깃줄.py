import sys
input = sys.stdin.readline

N = int(input())
line = []
for i in range(N):
    line.append(list(map(int,input().split())))
    
line.sort(key = lambda x:x[0])
answer = [0]*501
for j,k in line:
    answer[k] = max(answer[0:k])+1
        
print(N-max(answer))