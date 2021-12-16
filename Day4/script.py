def Decompose(file):
    File = open(file,"r")
    Instructions = File.read()
    Instructions = Instructions.split("\n\n")
    for i in range(1,len(Instructions)):
        Instructions[i] = Instructions[i].split("\n")
        for k in range(len(Instructions[i])):
            Instructions[i][k] = Instructions[i][k].split()
    Instructions[-1].pop(-1)
    return Instructions


def comp_list(a,b):
    for i in a:
        if i not in b:
            return False
    return True


def count_grid(a,b):
    res = 0
    for i in a:
        for j in i:
            if j not in b:
                res += int(j)
    return res * int(b[-1])

"Grids[Grille k ][Ligne j ][Colonne u ]"










def script1(file):
    Data = Decompose(file)
    AllPicked = Data[0].split(",")
    Picked = []
    AllGrids = Data[1:]
    for i in AllPicked:
        Picked.append(i)
        for k in range(len(AllGrids)):
            for j in range(len(AllGrids[k])):
                for u in range(len(AllGrids[k][j])):
                    if comp_list(AllGrids[k][:][u],Picked) == True or comp_list(AllGrids[k][j][:],Picked) == True:
                        print(count_grid(AllGrids[k],Picked))
                        return True
    print("Error")
    print(AllPicked)
    return False


def script2(file):
    Data = Decompose(file)
    AllPicked = Data[0].split(",")
    Picked = []
    AllGrids = Data[1:]
    AllGrids_Copy = AllGrids[:]
    for i in AllPicked:
        print(len(AllGrids))
        AllGrids = AllGrids_Copy[:]
        if len(AllGrids) == 3:
            for k in range(len(AllGrids)):
                for j in range(len(AllGrids[k])):
                    for u in range(len(AllGrids[k][j])):
                        coo = [AllGrids[k][0][u]] +[AllGrids[k][1][u]] +[AllGrids[k][2][u]] +[AllGrids[k][3][u]] +[AllGrids[k][4][u]]
                        if comp_list(coo,Picked) == True or comp_list(AllGrids[k][j][:],Picked) == True:
                            print(count_grid(AllGrids_Copy[0],Picked))
            Picked.append(i)
        else:
            Picked.append(i)
            for k in range(len(AllGrids)):
                for j in range(len(AllGrids[k])):
                    for u in range(len(AllGrids[k][j])):
                        coo =AllGrids[k][0][u] +AllGrids[k][1][u] +AllGrids[k][2][u] +AllGrids[k][3][u] +AllGrids[k][4][u]
                        if comp_list(coo,Picked) == True or comp_list(AllGrids[k][j][:],Picked) == True:
                            if AllGrids[k] in AllGrids_Copy:
                                AllGrids_Copy.remove(AllGrids[k])

    print("Finished")
    return False
script2('PuzzleInput1')
