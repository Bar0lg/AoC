import numpy as np
import sys,os,time,math,copy
def extract(file):
    f = open(file,"r")
    res = f.read().split("\n\n")
    Ins = res[1].split("\n")
    Ins.pop(-1)
    Paper = res[0].split("\n")
    for i in range(len(Paper)):
        Paper[i] = Paper[i].split(",")
    New_Ins = []
    for i in range(len(Ins)):
        New_Ins.append(Ins[i][11:].split("="))
    return New_Ins , Paper

def script(file):
    Ins , Cord = extract(file)
    xmax = 0
    ymax = 0
    for i in Cord:
        if int(i[0]) >= xmax:
            xmax = int(i[0])
        if int(i[1]) >= ymax:
            ymax = int(i[1])
    xmax +=1
    ymax +=1
    size = xmax * ymax
    Paper = np.zeros(size,dtype=int).reshape(ymax,xmax)
    for i in Cord:
        x = int(i[0])
        y = int(i[1])
        Paper[y][x] = 1
    print(len(Paper[Paper>=1]))

    for i in Ins:
        if i[0] == 'y':
            for y in range(int(i[1]),len(Paper)):
                for x in range(len(Paper[0])):
                    if Paper[y][x] == 1:
                        change = (y - int(i[1])) * 2
                        Paper[y-change][x] = 1
            Paper = Paper[:int(i[1]),]
        if i[0] == 'x':
            for y in range(len(Paper)):
                for x in range(int(i[1]),len(Paper[0])):
                    if Paper[y][x] == 1:
                        change = (x - int(i[1])) * 2
                        Paper[y][x-change] = 1
            Paper = Paper[:,:int(i[1])]
        print(len(Paper[Paper>=1]))
    print(Paper)
    return Paper

script("Input")
