import re
FILENAME = "4"
f = open("input/" + FILENAME + ".txt", "r")
lines = []
for line in f.readlines():
    lines.append(line.replace("\n", ""))


scratchCards = [1 for i in range(len(lines))]
card = 0
for line in lines:
    winningNums = set()
    hasNums = set()
    listLine = line.split(":")[1].split(" ")
    reachedMid = False
    score = 0
    for num in listLine:
        if ("|" in num):
            reachedMid = True
            continue
        elif num.isdigit():
            if reachedMid:
                hasNums.add(int(num))
            else:
                winningNums.add(int(num))
    for num in winningNums:
        if (num in hasNums):
           score += 1
    
    for i in range(score):
        scratchCards[card + 1 + i] += scratchCards[card]
    card += 1
    

    continue
print(sum(scratchCards))