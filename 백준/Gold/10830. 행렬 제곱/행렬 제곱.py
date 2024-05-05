A,B = map(int,input().split())

matrix = []
fm = []
for i in range(A):
    lst = list(map(int,input().split()))
    for j in range(len(lst)):
        lst[j]%=1000
    matrix.append(lst)
    fm.append(lst)
    
def mm(mtx1, mtx2):
    bm = [[0]*A for _ in range(A)]
    for i in range(A):
        for j in range(A):
            for k in range(A):
                bm[i][j] += mtx1[i][k]*mtx2[k][j]
                bm[i][j]%=1000
    return bm
def result(mtx,b):
    if b==1:
        return mtx
    if b%2==0:
        m = result(mtx,b//2)
        return mm(m,m)
    if b%2==1:
        m = result(mtx,b//2)
        return mm(mm(m,m),matrix)

res = result(matrix,B)
for i in range(len(res)):
    print(*res[i])