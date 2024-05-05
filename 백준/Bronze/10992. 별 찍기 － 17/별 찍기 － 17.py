a=int(input())
print(' '*(a-1)+'*')
if a>2:
    for i in range(1,a-1):
        print(' '*(a-i-1)+'*'+' '*(2*i-1)+'*')
if a>1:
    print('*'*(2*a-1))