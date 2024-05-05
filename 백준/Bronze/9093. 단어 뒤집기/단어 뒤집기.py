n=int(input())
for i in range(n):
    s=list(map(str,input().split()))
    for j in range(len(s)):
        for k in range(len(s[j])):
            print(s[j][len(s[j])-1-k],end="")
        print(' ', end="")
    print()