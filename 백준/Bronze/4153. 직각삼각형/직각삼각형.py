while(True):
    a = list(map(int,input().split()))
    mx = max(a)
    a.remove(mx)
    if (sum(a)==0):
        break
    elif(a[0]**2+a[1]**2 == mx**2):
        print("right")
    else:
        print("wrong")