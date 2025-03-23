import sys

N = int(sys.stdin.readline().strip())

for _ in range(N):
    wiki = dict()

    max_val = -1
    min_val = 99999

    W = str(sys.stdin.readline().strip())
    T = int(sys.stdin.readline().strip())

    for i, s in enumerate(list(W)):
        if s in wiki.keys():
            wiki[s].append(i)
        else:
            wiki[s] = [i]

    for idx in wiki.values():
        if len(idx) >= T:
            for i in range(len(idx) - T + 1):
                diff = idx[T+i-1] - idx[i] + 1
                if max_val < diff:
                    max_val = diff
                if min_val > diff:
                    min_val = diff

    if max_val == -1 and min_val == 99999:
         print(-1)
    else:
        print(min_val, max_val)