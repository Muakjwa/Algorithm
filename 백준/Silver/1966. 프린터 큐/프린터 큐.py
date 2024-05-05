num=int(input())
for i in range(num):
    n,m=map(int,input().split())
    lst=list(map(int,input().split()))
    count=0
    while True:
        if m==0:
            if lst[0]==max(lst):
                count+=1
                print(count)
                break
            else:
                lst.append(lst.pop(0))
                m=len(lst)-1
        elif lst[0]==max(lst):
            lst.pop(0)
            count+=1
            m-=1
        else:
            lst.append(lst.pop(0))
            m-=1