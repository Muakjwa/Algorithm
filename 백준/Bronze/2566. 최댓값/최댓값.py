import sys

grid = []

for _ in range(9):
    grid.append(list(map(int, sys.stdin.readline().strip().split())))

max_val = 0
row_val = 1
col_val = 1

for i, row in enumerate(grid):
    if max_val < max(row):
        max_val = max(row)
        row_val = i+1
        col_val = row.index(max(row)) + 1

print(max_val)
print(row_val, col_val)