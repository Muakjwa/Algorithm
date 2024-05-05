word=input()
lst=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
total=0
for i in word:
    for j in lst:
        for k in j:
            if i in k:
                total=total+lst.index(j)+3
print(total)