l = int(input())
lst=[]
while(l!=0):
    lst.append(str(l%10))
    l//=10
lst.sort(reverse = True)
print(''.join(lst))