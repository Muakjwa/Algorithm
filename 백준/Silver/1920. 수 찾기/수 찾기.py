n= int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int,input().split()))
a.sort()

for num in b:
    l, r = 0, n-1
    isExist = False
    
    while(l<=r):
        mid = (l+r)//2
        if(a[mid]==num):
            print(1)
            isExist=True
            break
        elif(a[mid]>num):
            r=mid-1
        else:
            l=mid+1
            
    if not isExist:
        print(0)
        