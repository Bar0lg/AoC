import numpy as np
import sys,os,time,math,copy

def extract(file):
    f = open(file,"r")
    tab = f.read().split("\n")
    tab.pop(-1)
    for i in range(len(tab)):
        tab[i] = [int(j) for j in tab[i]]
    tab = np.array(tab)

    return tab


def create_mega_map(tab):
    res = tab.copy()
    htab = tab.copy()
    for i in range(4):
        htab[:] += 1
        htab[htab > 9] = 1
        res = np.hstack((res,htab))
    vtab = res.copy()
    for i in range(4):
        vtab[:] += 1
        vtab[vtab > 9] = 1
        res = np.vstack((res,vtab))

    return res



def create_others_tab(tab):
    sizetab = tab.size
    shapetab = tab.shape
    distab = (np.ones(sizetab,dtype=int)*math.inf).reshape(shapetab)
    return distab, tab.shape


def script(file):
    tab = extract(file)
    tab = create_mega_map(tab)
    distab, finish_tuple = create_others_tab(tab)
    distab[0][0] = 0
    check = [(0,0)]
    neighbours_delta = [(1,0),(0,1),(-1,0),(0,-1)]
    while distab[finish_tuple[0]-1][finish_tuple[1]-1] == math.inf:
        #Find the lowest point ant put coordinate in coo
        coo = ()
        min = math.inf
        for i in check:
            if distab[i[0]][i[1]] < min:
                min = distab[i[0]][i[1]]
                coo = (i[0],i[1])

        check.remove(coo)
        #Check for borders and visited
        neighbours = []
        for i in neighbours_delta:
            if 0 <= coo[0]+i[0] <= (finish_tuple[0]-1) and 0 <= coo[1]+i[1] <= (finish_tuple[1]-1):
                if distab[coo[0]+i[0]][coo[1]+i[1]] == math.inf:
                    neighbours.append((coo[0]+i[0],coo[1]+i[1]))
                    check.append((coo[0]+i[0],coo[1]+i[1]))

        for i in neighbours:
            cooy = coo[0]
            coox = coo[1]
            neiy = i[0]
            neix = i[1]
            dist = distab[cooy][coox] + tab[neiy][neix]

            if distab[neiy][neix] >= dist:
                distab[neiy][neix] = dist

    return distab
#a = script("SampleInput15.txt")
b = script("RealInput15.txt")
print(b)
