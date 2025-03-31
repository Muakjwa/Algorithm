import sys

N = int(sys.stdin.readline().strip())

number = list(map(int, sys.stdin.readline().strip().split()))

number.sort()
cnt = 0

for i in range(len(number)):
    start = 0
    end = len(number)-1
    while start != end:
        if start == i:
            start += 1
        elif end == i:
            end -= 1
        elif number[start] + number[end] == number[i]:
            cnt += 1
            break
        elif number[start] + number[end] > number[i]:
            end -=1
        else:
            start +=1

print(cnt)