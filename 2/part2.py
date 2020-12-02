
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

    if p_max > len(pw):
        continue
    if p_min > len(pw):
        continue
    if (pw[p_min-1] == policy_ltr) != (pw[p_max-1] == policy_ltr):
        validcount += 1
    


print(validcount)