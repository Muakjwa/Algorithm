import sys
input = sys.stdin.readline

dictionary = [[[-1]*101 for _ in range(101)]for _ in range(101)]

def func(a,b,c):
    if dictionary[a+50][b+50][c+50]!=-1:
        return dictionary[a+50][b+50][c+50]
    if(a<=0 or b<=0 or c<=0):
        dictionary[a+50][b+50][c+50] = 1
        return 1
    elif(a>20 or b>20 or c>20):
        dictionary[a+50][b+50][c+50] = func(20,20,20)
        return dictionary[a+50][b+50][c+50]
    elif(a<b and b<c):
        dictionary[a+50][b+50][c+50] = func(a,b,c-1)+func(a,b-1,c-1)-func(a,b-1,c)
        return dictionary[a+50][b+50][c+50]
    else:
        dictionary[a+50][b+50][c+50] = func(a-1,b,c)+func(a-1,b-1,c)+func(a-1,b,c-1)-func(a-1,b-1,c-1)
        return dictionary[a+50][b+50][c+50]
while True:
    a,b,c = map(int,input().split())
    if(a==-1 and b==-1 and c==-1):
        break
    print('w('+', '.join(map(str,[a,b,c]))+') = '+str(func(a,b,c)))