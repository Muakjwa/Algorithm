N = int(input())

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result*=i
    return result

for i in range(N):
    a,b = map(int,input().split())
    print(factorial(b)//(factorial(b-a)*factorial(a)))