import re
FILENAME = "3"
f = open("input/" + FILENAME + ".txt", "r")
lines = []
for line in f.readlines():
    lines.append(line.replace("\n", ""))

data = [list(line) for line in lines]
partNumber = 0

def getAdjacentNumbers(data, r, c):
    numbers = []
    for r_new in range(r -1, r + 2):
        for c_new in range(c -1, c + 2):
            if (r_new < 0  or r_new >= len(data) or 
                c_new < 0 or c_new >= len(data)):
                continue
            if (data[r_new][c_new].isdigit()):
                number = data[r_new][c_new]
                data[r_new][c_new] = "."
                col = c_new - 1
                while 0 <= col and data[r_new][col].isdigit():
                    number = data[r_new][col] + number
                    data[r_new][col] = "."
                    col -= 1
                
                col = c_new + 1
                while col < len(data[0]) and data[r_new][col].isdigit():
                    number = number + data[r_new][col]
                    data[r_new][col] = "."
                    col += 1
                
                numbers.append(int(number))
    return numbers


for r in range(len(data)):
    for c in range(len(data[0])):
        if not (data[r][c].isdigit() or data[r][c] == "."):
            adjacentNumbers = getAdjacentNumbers(data, r, c)
            partNumber += sum(adjacentNumbers)

print(partNumber)