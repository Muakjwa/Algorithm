import sys

N = int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
card2 = list(map(int,sys.stdin.readline().split()))

card.sort()
exist= []

for i in card2:
    start, end = 0, N-1
    isExist = False
    while(start<=end):
        mid = (start+end)//2
        if(card[mid]==i):
            isExist = True
            break
        elif(card[mid]>i):
            end = mid-1
        else:
            start = mid +1
    exist.append(int(isExist))
    
print(*exist)