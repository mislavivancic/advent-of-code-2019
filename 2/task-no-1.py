f = open('input', "r")
code = f.readline().split(",")
code = [int(x) for x in code]
# init
code[1] = 12
code[2] = 2

for i in range(0, len(code), 4):
    if code[i] == 99:
        break
    
    if code[i] == 1:
        code[code[i+3]] = code[code[i+1]] + code[code[i+2]]
    
    if code[i] == 2:
        code[code[i+3]] = code[code[i+1]] * code[code[i+2]]
        
print(code[0])