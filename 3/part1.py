import sys

with open('input.txt', 'r') as f:
    mtn = f.readlines()

mtn = [r.strip() for r in mtn]
width = len(mtn[0])

trees = 0
for i, row in enumerate(mtn):
    col = (3 * i) % width
    if row[col] == '#':
        trees += 1

print(trees)
