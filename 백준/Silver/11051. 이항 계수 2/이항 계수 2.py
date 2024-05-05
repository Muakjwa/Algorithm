def factorial(n):
    re=1
    while(n>0):
        re*=n
        n-=1
    return re

n,k = map(int,input().split())
print((factorial(n)//(factorial(n-k)*factorial(k)))%10007)