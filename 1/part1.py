with open('input.txt', 'r') as f:
    input_list = f.readlines()

for idx, val in enumerate(input_list):
    for jdx, vall in enumerate(input_list[idx+1:]):
        if int(val) + int(vall) == 2020:
            print(int(val) * int(vall))