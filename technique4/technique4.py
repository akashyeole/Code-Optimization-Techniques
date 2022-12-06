# Unreachable code removal

# Opening the Input File in read mode
inputfile = open("technique4/technique4_input.txt", "r")
# Opening the Output File in write mode
outputfile = open("technique4/technique4_output.txt", "w")
# The flag that whether the upcoming lines should be included in the output program or not
removeFiles = False

# Iterating every line of thr input program
for line in inputfile:
    if(line.strip().endswith("}") and removeFiles):
        outputfile.write(line)
        removeFiles = False
    elif line.strip().endswith("{") or line.strip().endswith(")") or line.strip().endswith("){"): # Check if new block starts
        outputfile.write(line)
    elif line.strip() in ["break;", "continue;", "return 0;"]: # If any of these statements encounter then set flag
        if(line.strip() != "continue;"): # Don't print continue if it continue
            outputfile.write(line)
        removeFiles = True
    elif(not removeFiles): # If flag is set to false then add lines to the output files
        outputfile.write(line)

# Cloding the opened files
inputfile.close()
outputfile.close()