import sys
input = sys.stdin.readline

D = dict()

N, M = map(int,input().split())
for i in range(N):
    ID, PW = input().strip().split()
    D[ID] = PW
    
for i in range(M):
    ID = input().strip()
    print(D[ID])