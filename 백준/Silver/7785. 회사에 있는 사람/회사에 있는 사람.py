N = int(input())
s= set()

for _ in range(N):
    name, c = input().split()
    if c=='enter':
        s.add(name)
    elif c=='leave':
        s.remove(name)
        
for i in sorted(list(s),reverse=True):
    print(i)