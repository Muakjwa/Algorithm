while True:
    base = 1
    i=1
    try:
        n = int(input())
        while True:
            if base%n!=0:
                base*=10
                base+=1
                i+=1
            else:
                break
        print(i)
    except:
        break