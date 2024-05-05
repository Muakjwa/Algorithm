N = int(input())
even = N//2
odd = N - N//2

for i in range(N):
    print("* " * odd)
    print(" *" * even)