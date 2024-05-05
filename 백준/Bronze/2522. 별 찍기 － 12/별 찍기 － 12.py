a=int(input())
for i in range(a):
    print(' '*(a-i-1)+'*'*(i+1))
for i in range(a-1):
    print(' '*(i+1)+'*'*(a-i-1))