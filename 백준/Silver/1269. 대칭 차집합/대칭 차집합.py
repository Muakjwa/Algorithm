A, B = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

s = 0
s = len(set(a)-set(b)) + len(set(b)-set(a))
print(s)