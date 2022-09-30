def part1():
     File = open("measure.txt","r")

     Mesures = File.read()

     Mesures_list = Mesures.split("\n")

     res = []
     for i in range(1,len(Mesures_list)-1):
         if int(Mesures_list[i]) > int(Mesures_list[i-1]):
             res.append("I")
         else:
             res.append("D")

     nbI = 0
     for i in res:
         if i == "I":
             nbI += 1
     return nbI


def part2():
    file2 = open("measurePart2.txt","r")
    Mesures = file2.read()
    Mesures_list = Mesures.split("\n")

    res = []
    for i in range(len(Mesures_list)-4):
        sum1 = int(Mesures_list[i]) + int(Mesures_list[i+1]) + int(Mesures_list[i+2])
        sum2 = int(Mesures_list[i+1]) + int(Mesures_list[i+2]) + int(Mesures_list[i+3])
        if sum2 > sum1:
            res.append("I")
        elif sum2 < sum1:
            res.append("D")
        else:
            res.append("E")
    print(res)
    nbI = 0
    for i in res:
        if i == "I":
            nbI += 1
    return nbI

print(part2())
