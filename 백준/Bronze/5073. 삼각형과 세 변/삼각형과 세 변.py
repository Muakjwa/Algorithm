import sys

while True:
    a, b, c = map(int, sys.stdin.readline().strip().split())

    max_len = max(a, b, c)

    if a==0 and b==0 and c==0:
        break
    elif max_len * 2 >= (a+b+c):
        print("Invalid")
    elif a == b and b == c:
        print("Equilateral")
    elif a != b and b != c and c != a:
        print("Scalene")
    else:
        print("Isosceles")