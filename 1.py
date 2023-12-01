f = open("input/1.txt", "r")
lines = []
for line in f.readlines():
    lines.append(line)

sum = 0
for line in lines:
    integer = ""
    for c in line:
        if (c.isdigit()):
            integer+= c
            break
    for c in line[::-1]:
        if (c.isdigit()):
            integer += c
            break
    sum += int(integer)
print(sum)
# print(lines)