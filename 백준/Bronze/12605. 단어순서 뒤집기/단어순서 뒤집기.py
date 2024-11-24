import sys

N = int(sys.stdin.readline().strip())

for i in range(N):
    words = sys.stdin.readline().strip().split(' ')
    print(f"Case #{i+1}:", end=' ')
    for word in reversed(words):
        print(word, end = ' ')
    print()