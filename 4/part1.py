reqf = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

with open('input.txt', 'r') as f:
    data = f.readlines()

batches = []
curr = []
for line in data:
    currl = line.strip()
    if currl == "":
        batches.append(curr)
        curr = []
        continue
    else:
        pairs = currl.split(' ')
        keys = [p.split(':')[0] for p in pairs]
        curr = curr + keys
batches.append(curr)

count = 0
for b in batches:
    print(b)
    if 'cid' in b:
        b.remove('cid')
    if set(b) == reqf:
        count += 1

print(count)