lst = []
S = input()
for i in range(len(S)):
    lst.append(S[i:])
    
lst.sort()
for i in range(len(lst)):
    print(lst[i])