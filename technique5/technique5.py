# Compile Time Evaluation
import re # regular expression module
inputfile = open("technique5/technique5_input.txt", "r") # opening read file
outputfile = open("technique5/technique5_output.txt", "w") # opening write file
cons_var_table = {'+': '+', '-': '-', '/': '/', '%': '%', '*': '*'} # for storing the constant and their values and opertators
for line in inputfile:
    # Splitting line by '=' sign
    eq_separated_token = [token.strip() for token in line.strip().split('=')]
    if(len(eq_separated_token) > 1):
        # Splitting RHS by operators as delimeter
        operator_separated_token = [token.strip() for token in re.split(r"(/\s*|\+|-|\*|\%|\/)", eq_separated_token[1])]
        # Current expression of the line
        expression = " "
        for token in operator_separated_token:
            # Replacing the value for the variable if present in the dictionary
            if(cons_var_table.get(token) != None):
                expression += " " + cons_var_table[token]
            # Else keeping it as it is
            else:
                expression += " " + token
        try:
            # Trying to evaluate
            result = str(eval(expression))
            cons_var_table[eq_separated_token[0]] = result
        except:
            result = expression
        # Outputting the final line of code after updation
        outputfile.write(eq_separated_token[0] + ' = ' + result + '\n')
    else:
        outputfile.write(line)
inputfile.close()
outputfile.close()