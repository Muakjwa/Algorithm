import sys

val = 0

for _ in range(5):
    val += int(sys.stdin.readline().strip())

print(val)