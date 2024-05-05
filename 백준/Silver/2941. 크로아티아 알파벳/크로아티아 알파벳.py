word=input()
leng=len(word)
lst=['c=','c-','d-','lj','nj','s=','z=']
for i in lst:
    p=word.count(i)
    leng-=p
p=word.count('dz=')
leng-=p
print(leng)