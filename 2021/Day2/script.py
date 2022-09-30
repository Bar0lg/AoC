def Decompose(file):
    File = open(file,"r")
    Instructions = File.read()
    Instructions = Instructions.split("\n")
    Instructions.pop(-1)
    for i in range(len(Instructions)):
        Instructions[i] = Instructions[i].split()
    return Instructions

def Navigate1(file):
    Ins = Decompose(file)
    x = 0
    y = 0
    for i in Ins:
        if i[0] == "forward":
            x += int(i[1])
        elif i[0] == "down":
            y += int(i[1])
        elif i[0] == "up":
            y -= int(i[1])
    res = x * y
    return res

def Navigate2(file):
    Ins = Decompose(file)
    x = 0
    y = 0
    aim = 0
    for i in Ins:
        if i[0] == "forward":
            x += int(i[1])
            y += int(i[1]) * aim
        elif i[0] == "down":
            aim += int(i[1])
        elif i[0] == "up":
            aim -= int(i[1])
    res = x * y
    return res


print(Navigate2("PuzzleInput2.txt"))
