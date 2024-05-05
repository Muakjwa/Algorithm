A,B = map(int,input().split())
for i in range(A,0,-1):
    if A%i==0 and B%i==0:
        g= i
        break
print(g)
print(A*B//i)