L, C = map(int,input().split())

S = list(map(str,input().split()))
S.sort()

def c(k,l,s):
    if s==L:
        mo = k.count('a')+k.count('e')+k.count('i')+k.count('o')+k.count('u')
        if len(k)-mo >=2 and mo>=1:
            print(k)
        k=''
        return
    else:
        for i in range(l,C):
            c(k+S[i],i+1,s+1)
c('',0,0)