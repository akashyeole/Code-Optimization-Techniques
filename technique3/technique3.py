# Copy Propogation
import re
inputfile = open("technique3/technique3_input.txt", "r")
outputfile = open("technique3/technique3_output.txt", "w")
variables_table = {}
for line in inputfile:
    eq_separated_token = [token.strip() for token in line.strip().split('=')]
    if(len(eq_separated_token) > 1):
        operator_separated_token = [token.strip() for token in re.split(r"/\s*|\+|-|\*|\%|\/", eq_separated_token[1]) if token.strip().isalpha()]
        temp = eq_separated_token[1]
        for var in operator_separated_token:
            if(variables_table.get(var) != None):
                temp = temp.replace(var, variables_table[var])
        variables_table[eq_separated_token[0]] = temp
        outputfile.write(eq_separated_token[0] + " = " + temp + "\n")
    else:
        outputfile.write(line + "\n")
inputfile.close()
outputfile.close()