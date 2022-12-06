# Unreachable code removal
import re
inputfile = open("technique4/technique4_input.txt", "r")
outputfile = open("technique4/technique4_output.txt", "w")
variables_table = {}
stk = []
f = False
for line in inputfile:
    if(line.strip().endswith("}") and f):
        outputfile.write(line)
        f = False
    elif line.strip().endswith("()"):
        outputfile.write(line)
    elif line.strip().endswith("(){"):
        outputfile.write(line)
        stk += ['{']
    elif line.strip().endswith("{"):
        outputfile.write(line)
        stk += ['{']
    elif line.strip() in ["break;", "continue;", "return 0;"]:
        outputfile.write(line)
        f = True
    elif(not f):
        outputfile.write(line)
inputfile.close()
outputfile.close()