import sys

n1 = str(bin(int(sys.stdin.readline().strip()) + 16))[-4:]
n2 = str(bin(int(sys.stdin.readline().strip()) + 16))[-4:]
n3 = str(bin(int(sys.stdin.readline().strip()) + 16))[-4:]
print("{:04d}".format(int('0b' + n1 + n2 + n3 , 2)))