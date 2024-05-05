import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

lst.sort()
val = 0
i = 0

while True:
    if i >= N:
        break
    if i==N-1 and lst[i]<0:
        val+=lst[i]
        break
    if lst[i] < 0 and lst[i + 1] < 0:
        val += lst[i] * lst[i + 1]
        i += 2
    elif lst[i] < 0 and lst[i + 1] == 0:
        break
    elif lst[i] < 0 and lst[i + 1] > 0:
        val += lst[i]
        break
    else:
        break
lst.reverse()
i = 0
while True:
    if i >= N:
        break
    if i==N-1 and lst[i]>0:
        val+=lst[i]
        break
    if lst[i] > 0 and lst[i + 1] > 0:
        if lst[i]!= 1 and lst[i+1] !=1:
            val += lst[i] * lst[i + 1]
        else:
            val += (lst[i]+lst[i+1])
        i += 2
    elif lst[i] > 0 and lst[i + 1] <= 0:
        val += lst[i]
        break
    else:
        break

print(val)