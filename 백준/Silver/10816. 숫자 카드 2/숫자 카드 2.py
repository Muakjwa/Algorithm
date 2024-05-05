from collections import Counter

N = int(input())
card = list(map(int,input().split()))
M = int(input())
card2 = list(map(int,input().split()))

m = Counter(card)
l=[]
for i in range(M):
    l.append(m[card2[i]])

print(*l)