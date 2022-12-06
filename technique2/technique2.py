# Deadcode Elimination
import re       #importing regular expressions library
inputfile = open("technique2/technique2_input.txt", "r")    #read input file using read mode
outputfile = open("technique2/technique2_output.txt", "w")  #create a file to store output
variables_table = {}    #it is a dictionary to store the operands in it[Operand: used or not(true/false)]
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