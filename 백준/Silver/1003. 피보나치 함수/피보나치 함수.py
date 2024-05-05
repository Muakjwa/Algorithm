n=int(input())

def fib(num,p):
    if p[num]!=[0,0]:
        return p[num]
    if num==0:
        return p[0]
    elif num==1:
        return p[1]
    else:
        p[num][0]=fib(num-1,p)[0]+fib(num-2,p)[0]
        p[num][1]=fib(num-1,p)[1]+fib(num-2,p)[1]
        return p[num]
for _ in range(n):
    p=[[0,0] for i in range(41)]
    p[0],p[1]=[1,0],[0,1]
    num=int(input())
    print(fib(num,p)[0],fib(num,p)[1])
    