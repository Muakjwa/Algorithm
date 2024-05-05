n = int(input())
tri = []

for i in range(n):
    tri.append(list(map(int,input().split())))
    
for i in range(1,n):
    tri[i][0]+=tri[i-1][0]
    tri[i][-1]+=tri[i-1][-1]
    for j in range(1,i):
        tri[i][j]+=max(tri[i-1][j-1],tri[i-1][j])
        
print(max(tri[-1]))