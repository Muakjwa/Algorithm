import sys
input = sys.stdin.readline

wheel = []
for _ in range(4):
    w = str(input().strip())
    lst = []
    for i in range(8):
        lst.append(int(w[i]))
    wheel.append(lst)

K = int(input().strip())
idx = [0, 0, 0, 0]

for _ in range(K):
    n, d = map(int, input().strip().split())
    n-=1
    d*=-1
    idx_diff = [0, 0, 0, 0]
    idx_diff[n] = d
    n_tmp, d_tmp = n, d

    while True:
        n-=1
        if n < 0:
            break
        d *= -1
        if wheel[n][(idx[n] + 2) % 8] != wheel[n+1][(idx[n+1] - 2) % 8]:
            idx_diff[n] = d
        else:
            break

    while True:
        n_tmp+=1
        if n_tmp > 3:
            break
        d_tmp *= -1
        if wheel[n_tmp][(idx[n_tmp] - 2) % 8] != wheel[n_tmp-1][(idx[n_tmp-1] + 2) % 8]:
            idx_diff[n_tmp] = d_tmp
        else:
            break

    for i in range(4):
        idx[i] += idx_diff[i]

result = 0
for i in range(4):
    result += (wheel[i][(idx[i] % 8)] * (2**(i)))

print(result)