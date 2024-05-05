n=int(input())
i=n
while(i>0):
    print(" "*(n-i)+"*"*(2*i-1))
    i-=1
i+=1
while(i<n):
    i+=1
    print(" "*(n-i)+"*"*(2*i-1))
    