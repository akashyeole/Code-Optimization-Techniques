# Copy Propogation
import re
inputfile = open("technique3/technique3_input.txt", "r")
outputfile = open("technique3/technique3_output.txt", "w")
variables_table = {} #For Storing Variable values
for line in inputfile:
    eq_separated_token = [token.strip() for token in line.strip().split('=')] # Split into 2 sections 
    if(len(eq_separated_token) > 1):
        operator_separated_token = [token.strip() for token in re.split(r"/\s*|\+|-|\*|\%|\/", eq_separated_token[1]) if token.strip().isalpha()] # Seperationg the operand 
        temp = eq_separated_token[1] # Storing all RHS Side variables
        for var in operator_separated_token:
            if(variables_table.get(var) != None):
                temp = temp.replace(var, variables_table[var]) # If value of var in present in variable table then replace 
        variables_table[eq_separated_token[0]] = temp
        outputfile.write(eq_separated_token[0] + " = " + temp + "\n") # If any value is replaced then store that in temp 
    else:
        outputfile.write(line + "\n")
inputfile.close()
outputfile.close()