# Deadcode Elimination
import re
inputfile = open("technique2/technique2_input.txt", "r")
outputfile = open("technique2/technique2_output.txt", "w")
variables_table = {}
for line in inputfile:
    eq_separated_token = [token.strip() for token in line.strip().split('=')]
    if(len(eq_separated_token) > 1):
        variables_table[eq_separated_token[0]] = False
        operator_separated_token = [token.strip() for token in re.split(r"/\s*|\+|-|\*|\%|\/", eq_separated_token[1]) if token.strip().isalpha()]
        for var in operator_separated_token:
            variables_table[var] = True

inputfile = open("technique2/technique2_input.txt", "r")
for line in inputfile:
    eq_separated_token = [token.strip() for token in line.strip().split('=')]
    if(len(eq_separated_token) > 1):
        if variables_table[eq_separated_token[0]]:
            outputfile.write(line)
    else:
        outputfile.write(line)
inputfile.close()
outputfile.close()