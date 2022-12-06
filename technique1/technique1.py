# Constant Folding
import re
inputfile = open("technique1_input.txt", "r")
outputfile = open("technique1_output.txt", "w")
# constants_table : It stores all the constant in key-value pair
constants_table = {}
for line in inputfile :
    # this line split all the token and make  the new list of tokens
    tokens = [token.strip() for token in line.strip().split(' ')]
    # print(tokens)
    # In tokens it will check  for the #define.
    # If it is present then it then it stores the constant value  in constant_tables
    if(tokens[0] == "#define"):
        constants_table[tokens[1]] = tokens[2]
        # print(constants_table)
    else:
        # eq_separated : it stores the expression which is split by = and stores into the list
        eq_separated_data = [token.strip() for token in line.strip().split('=')]
        # print(eq_separated_data)
        #it stores the tokens separated by operator
        operator_separated_token = [token.strip() for token in re.split(r"/\s*|\+|-|\*|\%|\/", eq_separated_data[1])]
        # print(operator_separated_token)
        # temp : it will stored the eq_seperated token in index 1
        temp = eq_separated_data[1]
        # print(temp)

        for var in operator_separated_token:
            if(constants_table.get(var) != None):
                # it replace the var with the value in constant table
                temp = temp.replace(var, constants_table[var])
                # print(temp)
            
        try:
            # it compute the expression store in into the result
            result = eval(temp)
        except:
            result = temp

        outputfile.write(eq_separated_data[0] + " = " + str(result) + "\n")
inputfile.close()
outputfile.close()