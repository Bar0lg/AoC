import numpy as np
import copy

def decomp(file):
    rawdata = open(file,"r")
    readata = rawdata.read()
    data = readata.split("\n")
    data.pop(-1)
    for i in range(len(data)):
        data[i] = data[i].split(" -> ")
    for i in range(len(data)):
        for k in range(len(data[i])):
            data[i][k] = data[i][k].split(",")

    for i in range(len(data)):
        for k in range(len(data[i])):
            for j in range(len(data[i][k])):
                data[i][k][j] = int(data[i][k][j])
    return data

def create_tab(Ins):
    xmax = 0
    ymax = 0
    for i in Ins:
        for k in i:
            if k[0] > xmax:
                xmax = k[0]
            if k[1] > ymax:
                ymax = k[1]
    xmax += 1
    ymax += 1
    size = xmax * ymax
    tab = np.zeros(size,dtype=int).reshape(ymax,xmax)
    return tab


def add_to_line(tab,x1,x2,y):
    tab[y,x1:x2] += 1
    return tab
def add_to_column(tab,y1,y2,x):
    tab[y1:y2,x] += 1
    return tab

def add_to_dial_norm(tab,x,aug,y): #Pour diagonales comme sa /
    for i in range(aug-x):
        tab[y+i,x+i] += 1
    return tab
def add_to_dial_anti(tab,x1,x2,y1,y2):     #Pour les diagonales comme \
    for i,j in zip(range(x1,x2),range(y1,y2,-1)):
        tab[j,i] += 1
    return tab

"a = [[x1,y1],[x2,y2]]"

def check_which(a):
    if a[0][0] != a[1][0] and a[0][1] != a[1][1]:
        if (a[1][1] - a[0][1]) / (a[1][0] - a[0][0]) == 1:
            return "dn"
        elif (a[1][1] - a[0][1]) / (a[1][0] - a[0][0]) == -1 :
            return "da"
        else:
            return "E"
        return "d"  #Diagonal
    elif a[0][0] == a[1][0]:
        return "c"   #Column
    else:
        return "l"   #Line

def format_for_add(a,method):
    if method == "l":
        x = a[0][1]
        if a[0][0] <= a[1][0]:
            y1 = a[0][0]
            y2 = a[1][0]
        else:
            y1 = a[1][0]
            y2 = a[0][0]
        return y1,y2,x,None
    if method == "c":
        y = a[0][0]
        if a[0][1] <= a[1][1]:
            x1 = a[0][1]
            x2 = a[1][1]
        else:
            x1 = a[1][1]
            x2 = a[0][1]
        return y,None,x1,x2
    if method == "dn":
        if a[0][1] <= a[1][1]:
            x1 = a[0][0]
            x2 = a[1][0]
            y  = a[0][1]
            return x1,x2,y,None
        else:
            x1 = a[1][0]
            x2 = a[0][0]
            y  = a[1][1]
            return x1,x2,y,None
    if method == "da":
        if a[0][0] <= a[1][0]:
            x1 = a[0][0]
            x2 = a[1][0]
            y1 = a[0][1]
            y2 = a[1][1]
            return x1,x2,y1,y2
        else:
            x1 = a[1][0]
            x2 = a[0][0]
            y1 = a[1][1]
            y2 = a[0][1]
            return x1,x2,y1,y2
    if method == "E":
        return None,None,None,None

def script1(file):
    data = decomp(file)
    tab = create_tab(data)
    for i in data:
        method = check_which(i)
        x1,x2,y1,y2 = format_for_add(i,method)
        if method == "c":
            tab = add_to_column(tab,y1,y2+1,x1)
        if method == "l":
            tab = add_to_line(tab,x1,x2+1,y1)
        if method == "dn":
            tab = add_to_dial_norm(tab,x1,x2+1,y1)
        if method == "da":
            tab = add_to_dial_anti(tab,x1,x2+1,y1,y2-1)
        if method == "E":
            pass
    res = tab[tab >= 2]
    return tab ,len(res)

a , b = script1("Input")
print(a,b)
t = open("Tab","w")
"""
t = decomp("test")
tab = create_tab(t)
print(tab,"\n\n\n")
add_to_dial_anti(tab,7,10,9,6)
print(tab)
"""
