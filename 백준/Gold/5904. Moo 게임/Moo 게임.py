import sys

N = int(sys.stdin.readline().strip())
k = 1
len_moo = 3
len_moo_lst = [3]

while(True):
    if (N < 2 * len_moo + k + 3):
        break
    else:
        len_moo = 2 * len_moo + k + 3
        k += 1
        len_moo_lst.append(len_moo)

for len_moo_in_lst in reversed(len_moo_lst):
    if N > len_moo_in_lst + k + 3:
        N -= (len_moo_in_lst + k + 3)
    elif N > len_moo_in_lst:
        N -= len_moo_in_lst
    k -= 1

if N == 1:
    print('m')
else:
    print('o')