def Decompose(file):
    File = open(file,"r")
    Instructions = File.read()
    Instructions = Instructions.split("\n")
    Instructions.pop(-1)
    return Instructions


def bin_to_int(a):
    res = ""
    for i in a:
        res += str(i)
    return int(res,2)

def script1(file):
    Nb = Decompose(file)
    Gamma = []
    Epsilon = []
    for i in range(len(Nb[0])):
        Nb0 = 0
        for k in Nb:
            if k[i] == '0':
                Nb0 += 1
        if Nb0 > len(Nb)//2:
            Gamma.append(0)
            Epsilon.append(1)
        else:
            Gamma.append(1)
            Epsilon.append(0)
    print(Gamma)
    print(Epsilon)
    return bin_to_int(Gamma) * bin_to_int(Epsilon)




def Most_Least(List,choice):
    Most = []
    Least = []
    for i in range(len(List[0])):
        Nb0 = 0
        for k in List:
            if k[i] == '0':
                Nb0 += 1
        if Nb0 > len(List)//2:
            Most.append(0)
            Least.append(1)
        else:
            Most.append(1)
            Least.append(0)
    if choice == "most":
        return Most
    else:
        return Least








def script2(file):
    Nb = Decompose(file)
    Oxy = []
    CO2 = []
    PossibleOx = Nb[:]
    PossibleCO = Nb[:]
    Index = 0
    while len(PossibleOx) != 1:
        Oxy = Most_Least(PossibleOx,"most")
        PossOX_Copy = PossibleOx[:]
        for i in PossOX_Copy:
            if int(i[Index]) != int(Oxy[Index]):
                PossibleOx.remove(i)
        Index += 1


    Index = 0
    while len(PossibleCO) != 1:
        CO2 = Most_Least(PossibleCO,"least")
        PossCO_Copy = PossibleCO[:]
        for i in PossCO_Copy:
            if int(i[Index]) != int(CO2[Index]):
                PossibleCO.remove(i)
        Index += 1
    print(Oxy,CO2,PossibleCO , PossibleOx)




    return bin_to_int(PossibleCO) * bin_to_int(PossibleOx)

print(script2('PuzzleInput1.txt'))
