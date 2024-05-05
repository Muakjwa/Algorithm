a,b=map(int,input().split())
def pascal(n):
  if n==0:
    return[1]
  elif n==1:
    return[1,1]
  else:
    new=[]
    front=pascal(n-1)
    new.append(front[0])
    for i in range(n-1):
      new.append(front[i]+front[i+1])
    new.append(front[-1])
    return(new)
print(pascal(a-1)[b-1])