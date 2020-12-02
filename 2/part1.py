with open('input.txt', 'r') as f:
    inputdata = f.readlines()

print(inputdata)

validcount = 0
for line in inputdata:
    splitdata = line.split(':')
    policy_count = splitdata[0].split()[0]
    p_min = int(policy_count.split('-')[0])
    p_max = int(policy_count.split('-')[1])
    policy_ltr = splitdata[0].split()[1]
    pw = splitdata[1].strip()

    count = pw.count(policy_ltr)
    if count >= p_min and count <= p_max:
        validcount += 1

print(validcount)