import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int,input().split()))
l = list(set(num))
l.sort()
dic={}
for i in range(len(l)):
    dic[l[i]] = i
for k in num:
    print(dic[k],end=' ')
    