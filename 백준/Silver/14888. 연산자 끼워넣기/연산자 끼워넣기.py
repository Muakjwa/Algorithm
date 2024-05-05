n=int(input())
lst=list(map(int,input().split()))
p,m,mul,div=map(int,input().split())
result=[]
max_result=-1000000001
min_result=1000000001

def back(cnt,val,p,m,mul,div):
    global max_result
    global min_result
    if cnt==len(lst):
        max_result=max(max_result,val)
        min_result=min(min_result,val)
        return
    if p:
        back(cnt+1,val+lst[cnt],p-1,m,mul,div)
    if m:
        back(cnt+1,val-lst[cnt],p,m-1,mul,div)
    if mul:
        back(cnt+1,val*lst[cnt],p,m,mul-1,div)
    if div:
        back(cnt+1,-(-val//lst[cnt]) if val<0 else val//lst[cnt],p,m,mul,div-1)
back(1,lst[0],p,m,mul,div)
print(max_result)
print(min_result)