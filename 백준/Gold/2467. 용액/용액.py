import sys

N = int(sys.stdin.readline().strip())

Sol = list(map(int, sys.stdin.readline().strip().split()))

reversed_Sol = list(reversed(Sol))

i = 0
j = 0

result = 3000000000
res_x = -1
res_y = -1

while Sol[i] != reversed_Sol[j]:
    val = Sol[i] + reversed_Sol[j]
    if abs(val) < result:
        result = abs(val)
        res_x = Sol[i]
        res_y = reversed_Sol[j]
    if val == 0:
        break
    elif val > 0:
        j += 1
    else:
        i += 1

print(res_x, res_y)