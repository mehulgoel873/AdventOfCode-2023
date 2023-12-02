f = open("input/1_2.txt", "r")
lines = []
for line in f.readlines():
    lines.append(line)

sum = 0
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for line in lines:
    print()
    origLine = line
    integer = ""
    while (line != ""):
        cont = True
        if (line[0].isdigit()):
            integer+=line[0]
            break
        for i in range(9):
            if numbers[i] == line[:len(numbers[i])]:
                integer += str(i + 1)
                cont = False
                break
        if (not cont):
            break
        line = line[1:]
    line = origLine
    while (line != ""):
        # print(line)
        cont = True
        if (line[-1].isdigit()):
            integer+=line[-1]
            break
        for i in range(9):
            string = line[-1 * len(numbers[i]):]
            # print(line[-1 * len(numbers[i]) - 1:-1])
            if numbers[i] == string:
                integer += str(i + 1)
                cont = False
                break
        if (not cont):
            break
        line = line[:-1]
    # print(integer)
    sum += int(integer)
print(sum)
# print(lines)