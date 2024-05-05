a,b=map(int,input().split())
c=list(map(int,input().split()))
p=0
o=0
s=0
for i in range(p,a-2):
    u=p
    p+=1
    for j in range(1+u,a-1):
        o=u
        u+=1
        for k in range(2+o,a):
            o+=1
            max= int(c[i]+c[j]+c[k])
            if max <= b:
                if max > s:
                    s=max

print(s)