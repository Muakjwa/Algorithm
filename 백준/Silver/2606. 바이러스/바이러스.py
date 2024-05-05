n=int(input())
ln=int(input())
lst=[[] for i in range(n+1)]
mp=[1]
for i in range(ln):
    n1,n2=map(int,input().split())
    lst[n1].append(n2)
    lst[n2].append(n1)
    
def dfs(graph,st_num,lest):
    for i in graph[st_num]:
        if i not in lest:
            lest.append(i)
            dfs(graph,i,lest)
    return lest
print(len(dfs(lst,1,mp))-1)