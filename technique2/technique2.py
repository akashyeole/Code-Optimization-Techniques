# Deadcode Elimination
import re       #importing regular expressions library
inputfile = open("technique2/technique2_input.txt", "r")    #read input file using read mode
outputfile = open("technique2/technique2_output.txt", "w")  #create a file to store output
variables_table = {}    #it is a dictionary to store the operands in it[Operand: used or not(true/false)]
for line in inputfile:
    eq_separated_token = [token.strip() for token in line.strip().split('=')]   #split output based on '='
    if(len(eq_separated_token) > 1): 
        if(variables_table.get(eq_separated_token[0]) == None):     # if the variable is already present in the table then no need to add it as false kepp it as it is
            variables_table[eq_separated_token[0]] = False      #set unused operands as false
        operator_separated_token = [token.strip() for token in re.split(r"/\s*|\+|-|\*|\%|\/", eq_separated_token[1]) if token.strip().isalpha()]       #split expression based on the operator and store the operands in the eq_separated_tokens folder
        for var in operator_separated_token:
            variables_table[var] = True     #set operands which are used/assigned as True

inputfile = open("technique2/technique2_input.txt", "r")        #again open the input file
for line in inputfile:
    eq_separated_token = [token.strip() for token in line.strip().split('=')]   
    if(len(eq_separated_token) > 1):
        if variables_table[eq_separated_token[0]]:      #if operand is used then print it in the output file
            outputfile.write(line)
    else:
        outputfile.write(line)
inputfile.close()
outputfile.close()