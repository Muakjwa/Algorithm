import sys
input = sys.stdin.readline

N, M = map(int,input().split())
nlist = list(map(int,input().split()))
mlist = list(map(int,input().split()))

nlist += mlist
nlist.sort()
print(*nlist)