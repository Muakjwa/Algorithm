N = int(input())
paper = []

for i in range(N):
    paper.append(list(map(int,input().split())))
    
id_minus = 0
id_zero = 0
id_one = 0

def div(x,y,z):
    global id_minus, id_zero, id_one
    n = paper[x][y]
    for i in range(x,x+z):
        for j in range(y,y+z):
            if(paper[i][j]!=n):
                for k in range(3):
                    for p in range(3):
                        div(x+k*z//3,y+p*z//3,z//3)
                return
    if(n == 1):
        id_one+=1
    elif(n==0):
        id_zero+=1
    else:
        id_minus+=1
        
div(0,0,N)
print(id_minus)
print(id_zero)
print(id_one)