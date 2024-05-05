pipe = list(input())
piece = []
cnt=0
for i in range(len(pipe)):
    if pipe[i]=='(':
        piece.append('(')
    else:
        if pipe[i-1]=='(':
            piece.pop()
            cnt+=len(piece)
        else:
            piece.pop()
            cnt+=1
print(cnt)