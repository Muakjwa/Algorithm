N = int(input())
rope=[]
for _ in range(N):
    rope.append(int(input()))
rope.sort(reverse=True)
result = 0
for i in range(N):
    result = max(result, (i+1)*rope[i])
    
print(result)