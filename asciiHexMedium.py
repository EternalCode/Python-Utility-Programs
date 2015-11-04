with open('C:/Table.txt') as f:
    lines = f.read().splitlines()
for i in range (0, len(lines)):
    lines[i] = lines[i].split('=')
convert = raw_input("enter string: ")
result = ""
check_version = raw_input('hex to ascii or ascii to hex?')
if (check_version == "1"):
    for char in convert:
        for element in lines:
            if element[1] == char:
                result += (element[0])
    print(result)
else:
    #take 2 letters at a time from convert
    counter = 0
    #strip whitespace from convert
    convert = convert.replace(" ", "")
    while counter < len(convert):
        for element in lines:
            if element[0] == (convert[counter:counter+2]):
                result += (element[1])
        counter += 2
    print(result)
