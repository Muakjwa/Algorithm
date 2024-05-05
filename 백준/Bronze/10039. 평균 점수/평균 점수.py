a = []
j=0
for i in range(0,5):
    a.append(int(input()))
for k in range(0,5):
    if(a[k]<40):
        a[k]=40
    j+=int(a[k])
print(int(j/5))