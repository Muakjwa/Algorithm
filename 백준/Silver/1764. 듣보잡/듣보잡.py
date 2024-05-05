N, M = map(int,input().split())
hear = set()
see = set()

for i in range(N):
    hear.add(input())
for i in range(M):
    see.add(input())

hear_see = sorted(list(hear & see))

print(len(hear_see))
for i in range(len(hear_see)):
    print(hear_see[i])