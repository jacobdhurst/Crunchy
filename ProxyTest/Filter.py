inputFile = open("unfiltered.txt", "r")
outputFile = open("filtered.txt", "w")

length = 0;
temp = new = ""

for line in inputFile:
    for char in line:
        if char == ":" or char == "." or char.isdigit(): temp += char
    length = len(temp)
    if length > 10:
        temp = temp[:length - 4] + ":" + temp[length - 4:]
        temp += "\n"
        new += temp
    temp = ""

outputFile.write(new)