import sys
input = sys.stdin.readline

N = int(input())
seed = list(input().strip())
for i in range(N-1):
    s = list(input().strip())
    for j in range(len(seed)):
        if(seed[j] != s[j]):
            seed[j]='?'
print(''.join(seed))