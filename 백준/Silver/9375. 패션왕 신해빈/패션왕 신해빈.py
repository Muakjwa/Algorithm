N = int(input())
for i in range(N):
    T = int(input())
    dictionary = {}
    val=1
    for j in range(T):
        cloth = list(input().split(' '))
        if cloth[1] in dictionary:
            dictionary[cloth[1]]+=1
        else:
            dictionary[cloth[1]]=1
    for i in dictionary.values():
        val*=(i+1)
    val-=1
    print(val)