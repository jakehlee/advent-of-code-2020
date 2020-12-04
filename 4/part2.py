reqf = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

with open('input.txt', 'r') as f:
    data = f.readlines()

batches = []
curr = {}
for line in data:
    currl = line.strip()
    if currl == "":
        batches.append(curr)
        curr = {}
        continue
    else:
        pairs = currl.split(' ')
        for p in pairs:
            curr[p.split(':')[0]] = p.split(':')[1]
batches.append(curr)


# Validation
count = 0
for b in batches:

    # Key validation
    keys = b.keys()
    if 'cid' in keys:
        b.pop('cid')
    if set(keys) != reqf:
        continue

    # byr val
    try:
        byr = int(b['byr'])
        assert(byr >= 1920)
        assert(byr <= 2002)
    except Exception:
        continue
    

    # iyr val
    try:
        iyr = int(b['iyr'])
        assert(iyr >= 2010)
        assert(iyr <= 2020)
    except Exception:
        continue

    # eyr val
    try:
        eyr = int(b['eyr'])
        assert(eyr >= 2020)
        assert(eyr <= 2030)
    except Exception:
        continue

    # hgt
    try:
        hgt = b['hgt']
        if hgt[-2:] == 'cm':
            assert(int(hgt[:-2]) >= 150)
            assert(int(hgt[:-2]) <= 193)
        elif hgt[-2:] == 'in':
            assert(int(hgt[:-2]) <= 76)
            assert(int(hgt[:-2]) >= 59)
        else:
            assert(1 == 0)
    except Exception:
        continue
    
    # hcl
    try:
        hcl = b['hcl']
        assert(hcl[0] == '#')
        for c in hcl[1:]:
            assert(c in '01234567890abcdef')
        
    except Exception:
        continue
    
    # ecl
    try:
        ecl = b['ecl']
        assert(ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
        
    except Exception:
        continue
    
    # pid
    try:
        pid = b['pid']
        assert(int(pid))
        assert(len(pid) == 9)

    except Exception:
        continue

    print(b)
    count += 1

print(count)