# Constant Folding
import re
inputfile = open("technique1/technique1_input.txt", "r")
outputfile = open("technique1/technique1_output.txt", "w")
constants_table = {}
for line in inputfile:
    tokens = [token.strip() for token in line.strip().split(' ')]
    if(tokens[0] == "#define"):
        constants_table[tokens[1]] = tokens[2]
    else:
        eq_separated_data = [token.strip() for token in line.strip().split('=')]
        operator_separated_token = [token.strip() for token in re.split(r"/\s*|\+|-|\*|\%|\/", eq_separated_data[1])]
        temp = eq_separated_data[1]
        for var in operator_separated_token:
            if(constants_table.get(var) != None):
                temp = temp.replace(var, constants_table[var])
            
        try:
            result = eval(temp)
        except:
            result = temp

        outputfile.write(eq_separated_data[0] + " = " + str(result) + "\n")
inputfile.close()
outputfile.close()