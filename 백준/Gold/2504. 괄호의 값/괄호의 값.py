import sys
input = sys.stdin.readline

gwalho,num,idx=[],[],[]
n,k,index=0,1,31

line = input().strip()
for i in line:
    if i=='(':
        if k!=1:
            num.append(k)
            idx.append(len(gwalho)-1)
            k=1
        gwalho.append(i)
    elif i =='[':
        if k!=1:
            num.append(k)
            idx.append(len(gwalho)-1)
            k=1
        gwalho.append(i)
    elif i==')' and gwalho!=[] and gwalho.pop() == '(':
        if len(gwalho) in idx:
            for i in range(len(idx)):
                if idx[i]==len(gwalho):
                    k=k+num[i]
                    num[i]=0
            k*=2
        else:
            k*=2
    elif i==']' and gwalho!=[] and gwalho.pop()=='[':
        if len(gwalho) in idx:
            for i in range(len(idx)):
                if idx[i] == len(gwalho):
                    k = k + num[i]
                    num[i] = 0
            k*=3
        else:
            k*=3
    else:
        k=0
        break

if k ==0 or gwalho!=[]:
    print(0)
else:
    print(k+sum(num))