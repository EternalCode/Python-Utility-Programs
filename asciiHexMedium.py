with open('C:/Users/Dilshan/Documents/Hack/Sprites/Table.txt') as f:
    lines = f.read().splitlines()
for i in range (0, len(lines)):
    lines[i] = lines[i].split('=')
convert = raw_input("enter string: ")
result = ""
check_version = raw_input('H2A or A2H?')
if (check_version == "1"):
    for char in convert:
        for element in lines:
            if element[1] == char:
                result += (element[0])
    print(result)
else:
    convert = convert.split(" ")
    for index in convert:
        for element in lines:
            if element[0] == index:
                result += (element[1])
    print(result)