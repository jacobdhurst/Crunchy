def main():
    input_file = open("ProxyList.txt", "r+")
    output_file = open("FilteredProxyList.txt", "w+")

    temp = new = ""

    for line in input_file:
        for char in line:
            if char == ":" or char == "." or char.isdigit(): temp += char

        length = len(temp)

        if length > 10:
            # temp = temp[:length - 4] + ":" + temp[length - 4:]
            temp += "\n"
            new += temp
            temp = ""

    output_file.write(new)
    input_file.close()
    output_file.close()
