first = list(input())
second = list(input())
total = [[0 for _ in range(len(second)+1)] for _ in range(len(first)+1)]

for i in range(len(first)):
    for j in range(len(second)):
        if(first[i]==second[j]):
            total[i+1][j+1] = total[i][j]+1
        else:
            total[i+1][j+1] = max(total[i+1][j], total[i][j+1])

            
print(total[-1][-1])