N = int(input())
N//=3

e = ['  *  ',' * * ','*****']

while N>1:
    blank = len(e[-1])//2+1
    l = len(e)
    for i in range(len(e)):
        e.append(e[i]+' '+e[i])
    for i in range(l):
        e[i] = ' '*blank+e[i]+' '*blank
    N//=2
for i in e:
    print(i)