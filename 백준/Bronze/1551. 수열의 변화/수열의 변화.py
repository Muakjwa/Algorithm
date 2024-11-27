import sys

N, time = map(int, sys.stdin.readline().strip().split(' '))

numbers = list(map(int, sys.stdin.readline().strip().split(',')))

def diff(numbers):
    new_numbers = []
    for i in range(1, len(numbers)):
        new_numbers.append(numbers[i] - numbers[i-1])
    return new_numbers

for _ in range(time):
    numbers = diff(numbers)

print(','.join(list(map(str,numbers))))