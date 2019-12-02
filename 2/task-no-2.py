import copy

f = open('input', "r")
code = f.readline().split(",")
code = [int(x) for x in code]
# init

for noun in range(0,99):
    for verb in range(0,99):
        temp_code = copy.deepcopy(code)
        temp_code[1] = noun
        temp_code[2] = verb

        for i in range(0, len(temp_code), 4):
            if temp_code[i] == 99:
                break
    
            if temp_code[i] == 1:
                temp_code[temp_code[i+3]] = temp_code[temp_code[i+1]] + temp_code[temp_code[i+2]]
    
            if temp_code[i] == 2:
                temp_code[temp_code[i+3]] = temp_code[temp_code[i+1]] * temp_code[temp_code[i+2]]
        
        if temp_code[0] == 19690720:
            print(100*noun+verb)
