import sys
import re

N = int(sys.stdin.readline().strip())
num_list = []

for _ in range(N):
    num_list += re.findall(r'\d+', sys.stdin.readline().strip())

for num in sorted(map(int,num_list)):
    print(int(num))