import sys
input = sys.stdin.readline

S = input().rstrip()
string = ''
str_set = set()

for i in range(len(S)):
    string = ''
    for j in range(i,len(S)):
        string+=S[j]
        if string not in str_set:
            str_set.add(string)
print(len(str_set))