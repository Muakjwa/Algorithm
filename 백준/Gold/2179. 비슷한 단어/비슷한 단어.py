import sys

N = int(sys.stdin.readline().strip())

words = []

for _ in range(N):
    words.append(str(sys.stdin.readline().strip()))

words_original = words.copy()
words.sort()

maxlen = -1
f = ""
b = ""

for i in range(N-1):
    cnt = 0
    for j in range(min(len(words[i]), len(words[i+1]))):
        if words[i][j] == words[i+1][j]:
            cnt+=1
        else:
            break
    if cnt > maxlen:
        f = words[i]
        b = words[i+1]
        maxlen = cnt

out = 0
for i in range(N-1):
    if out == 1:
        break
    for j in range(i+1, N):
        if len(words_original[i]) >= maxlen and len(words_original[j]) >= maxlen:
            if words_original[i][:maxlen] == words_original[j][:maxlen]:
                print(words_original[i])
                print(words_original[j])
                out = 1
                break