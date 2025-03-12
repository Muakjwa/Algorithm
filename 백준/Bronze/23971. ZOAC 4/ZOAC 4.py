import sys

H, W, N, M = map(int, sys.stdin.readline().strip().split())

H_avail = H//(N+1) + (1 if (H%(N+1))>0 else 0)
W_avail = W//(M+1) + (1 if (W%(M+1))>0 else 0)

print(H_avail * W_avail)