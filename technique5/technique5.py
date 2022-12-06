# Compile Time Evaluation
import re
inputfile = open("technique5/technique5_input.txt", "r")
outputfile = open("technique5/technique5_output.txt", "w")
loop = False
cons_var_table = {'+': '+', '-': '-', '/': '/', '%': '%', '*': '*'}
for line in inputfile:
    eq_separated_token = [token.strip() for token in line.strip().split('=')]
    if(len(eq_separated_token) > 1):
        operator_separated_token = [token.strip() for token in re.split(r"(/\s*|\+|-|\*|\%|\/)", eq_separated_token[1])]
        expression = " "
        for token in operator_separated_token:
            # print(token)
            if(cons_var_table.get(token) != None):
                expression += " " + cons_var_table[token]
            else:
                expression += " " + token
        try:
            result = str(eval(expression))
            cons_var_table[eq_separated_token[0]] = result
        except:
            result = expression
        outputfile.write(eq_separated_token[0] + ' = ' + result + '\n')
    else:
        outputfile.write(line)
inputfile.close()
outputfile.close()