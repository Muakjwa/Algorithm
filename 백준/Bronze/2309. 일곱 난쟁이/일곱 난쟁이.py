a=[]
for i in range(9):
    a.append(int(input()))
for i in range(9):
    for j in range(9):
        if i!=j:
            if sum(a)-a[i]-a[j]==100:
                b,c=i,j
if b>c:
    del a[b]
    del a[c]
else:
    del a[c]
    del a[b]
a.sort()
for i in range(7):
    print(a[i])