N = int(input())
lst=[]

for i in range(N):
    lst.append(str(input()))
    
def div(x,y,z):
    size = lst[x][y]
    for i in range(x,x+z):
        for j in range(y,y+z):
            if(lst[i][j]!=size):
                print("(",end="")
                for k in range(2):
                    for p in range(2):
                        div(x+k*z//2, y+p*z//2, z//2)
                print(")",end="")
                return
    if(size =='1'):
        print('1',end="")
    else:
        print('0',end="")
        
div(0,0,N)