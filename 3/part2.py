import sys

with open('input.txt', 'r') as f:
    mtn = f.readlines()

mtn = [r.strip() for r in mtn]
width = len(mtn[0])

answer = 1

trees = 0
for i, row in enumerate(mtn):
    col = (1 * i) % width
    if row[col] == '#':
        trees += 1
print(trees)
answer = answer * trees

trees = 0
for i, row in enumerate(mtn):
    col = (3 * i) % width
    if row[col] == '#':
        trees += 1
print(trees)
answer = answer * trees

trees = 0
for i, row in enumerate(mtn):
    col = (5 * i) % width
    if row[col] == '#':
        trees += 1
print(trees)

answer = answer * trees

trees = 0
for i, row in enumerate(mtn):
    col = (7 * i) % width
    if row[col] == '#':
        trees += 1
print(trees)

answer = answer * trees

trees = 0
for i, row in enumerate(mtn):
    if i % 2:
        continue
    col = int((i / 2) % width)
    if row[col] == '#':
        trees += 1
print(trees)

answer = answer * trees

print(answer)
