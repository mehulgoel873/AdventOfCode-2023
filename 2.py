import re
FILENAME = "2"
f = open("input/" + FILENAME + ".txt", "r")
lines = []
for line in f.readlines():
    lines.append(line.replace("\n", ""))

sumPower = 0
for line in lines:
    sections = re.split('; |: ', line)
    ID = int(sections[0][5:])
    valid = True
    maxes = [0, 0, 0]
    for section in sections[1:]:
        pieces = [x.split(" ") for x in section.split(", ")]
        for play in pieces:
            if (play[1] == "blue"):
                maxes[2] = max(maxes[2], int(play[0]))
            elif (play[1] == "green"):
                maxes[1] = max(maxes[1], int(play[0]))
            elif (play[1] == "red"):
                maxes[0] = max(maxes[0], int(play[0]))
            if not valid: break
        if not valid: break
        continue
    if valid: 
        sumPower += maxes[0] * maxes[1] * maxes[2]
    pass
print(sumPower)
# print(lines)