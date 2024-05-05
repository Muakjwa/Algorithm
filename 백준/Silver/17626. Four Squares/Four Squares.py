INF = 1e9
N = int(input())
square = [0,1]
for i in range(2,N+1):
    j=1
    S=INF
    while j**2<=i:
        S = min(S, square[i-j**2]+1)
        j+=1
    square.append(S)
print(square[N])