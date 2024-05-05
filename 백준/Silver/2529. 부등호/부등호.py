#백준 2529 브루트포스
n=int(input())
s=list(map(str,input().split()))
num=[]
for i in range(n):
    num.append(list())
for i in range(10):
    for j in range(10):
        if s[0]=='<':
            if i>j:
                num[0].append([j,i])
        else:
            if i>j:
                num[0].append([i,j])
def play(n):
    if n>1:
        play(n-1)
    for i in range(10):
        for j in range(len(num[n-1])):
            if i not in num[n-1][j]:
                if s[n]=='<':
                    if num[n-1][j][-1]<i:
                        num[n].append(num[n-1][j]+[i])
                else:
                    if num[n-1][j][-1]>i:
                        num[n].append(num[n-1][j]+[i])
play(n-1)
set=[]
nu=num[-1]
for i in range(len(nu)):
    st=''
    for j in range(len(nu[i])):
        st=st+str(nu[i][j])
    set.append(st)
inte=[]
for i in range(len(set)):
    inte.append(int(set[i]))
print(set[inte.index(max(inte))])
print(set[inte.index(min(inte))])