import numpy as np
import sys,os,time,math,copy

def extract(file):
    f = open(file,"r")
    res = f.read().split("\n\n")
    Sample = res[0]
    Table = res[1].split("\n")
    Table.pop(-1)
    for i in range(len(Table)):
        Table[i] = Table[i].split(" -> ")
    return Sample,Table

def script(file,step):
    Sample , Table = extract(file)
    Count = {}
    RealTable = {}
    Count_Letters = {}
    for i in Table:
        Count[i[0]] = 0
        RealTable[i[0]] = [i[0][0]+i[1],i[1]+i[0][1]]


    for i in range(len(Sample)-1):
        p = Sample[i] + Sample[i+1]
        Count[p] += 1

    for i in range(step):
        Count_Copy = copy.deepcopy(Count)
        for j in Count_Copy:
            a = RealTable[j][0]
            b = RealTable[j][1]
            Count[j] -= Count_Copy[j]
            Count[a] += (1 * Count_Copy[j])
            Count[b] += (1 * Count_Copy[j])

    print(Count)
    for i in Count:
        if i[0] not in Count_Letters:
            Count_Letters[i[0]] = 0
        if i[1] not in Count_Letters:
            Count_Letters[i[1]] = 0
        Count_Letters[i[0]] += Count[i]
        Count_Letters[i[1]] += Count[i]

    First_Letter = Sample[0]
    Last_Letter = Sample[-1]
    for i in Count_Letters:
        Count_Letters[i] = Count_Letters[i] // 2
    Count_Letters[First_Letter] += 1
    Count_Letters[Last_Letter] += 1


    minElem = math.inf
    MaxElem = 0
    for i in Count_Letters:
        if Count_Letters[i] > MaxElem:
            MaxElem = Count_Letters[i]
        if Count_Letters[i] < minElem:
            minElem = Count_Letters[i]
    res = MaxElem - minElem
    return Count_Letters,res
r ,p= script("Input",40)
print(r,p)
