def execute(input):
    temp = new = ""
    for line in input:
        for char in line:
            if char == ":" or char == "." or char.isdigit(): temp += char
        length = len(temp)
        if length > 10:
            temp = temp[:length - 4] + ":" + temp[length - 4:]
            temp += "\n"
            new += temp
            temp = ""
        input.write(new)