N, r, c = map(int,input().split())

def re(r,c):
    if r==0 and c==0:
        return 0
    if r%2==0 and c%2==0:
        return 4*re(r//2,c//2)
    elif r%2==1:
        return re(r-1,c)+2
    elif c%2==1:
        return re(r,c-1)+1
print(re(r,c))