N = int(input())
string = input()
S = 0

for i in range(N):
    S+=((ord(string[i])-96)*(31**i))
    S = S%1234567891
print(S)