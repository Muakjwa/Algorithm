N = int(input())
lst=[]

for i in range(N):
    lst.append(list(map(int,input().split())))
white = 0
blue = 0
    
def div(x,y,n):
    global white, blue
    num = lst[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if(lst[i][j]!=num):
                for k in range(2):
                    for p in range(2):
                        div(x+k*n//2, y+p*n//2, n//2)
                return
    if(num==1):
        blue+=1
    else:
        white+=1
        
div(0,0,N)

print(white)
print(blue)