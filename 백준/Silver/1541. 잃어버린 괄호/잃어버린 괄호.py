string = input().split('-')
lst = []

for i in string:
    cnt= 0
    s = i.split('+')
    for j in s:
        cnt+=int(j)
    lst.append(cnt)
l = lst[0]
for i in range(1,len(lst)):
    l-=lst[i]
print(l)