import itertools

with open('input.txt', 'r') as f:
    input_list = f.readlines()

input_list = [int(i) for i in input_list]

threesets = list(itertools.combinations(input_list, 3))

for s in threesets:
    if sum(s) == 2020:
        print(s[0] * s[1] * s[2])