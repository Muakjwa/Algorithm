import sys

line = sys.stdin.readline().strip()

happy = line.count(':-)')
unhappy = line.count(':-(')

if happy == 0 and unhappy == 0:
    print("none")
elif happy == unhappy:
    print("unsure")
elif happy > unhappy:
    print("happy")
elif unhappy > happy:
    print("sad")