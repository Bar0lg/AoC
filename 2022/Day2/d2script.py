import sys,os,time,math,copy
import numpy as np

def extract(file):
    f = open(file,"r").read().split("\n")
    data = [i.split(" ") for i in f]
    return data


VALUES = {'X':1,'Y':2,'Z':3}

TABLE = {'A':{'X':3,'Y':6,'Z':0},'B':{'X':0,'Y':3,'Z':6},'C':{'X':6,'Y':0,'Z':3}}

P2OUTCOME = {'X':0,'Y':3,'Z':6}

P2VAL = {'X':-1,'Y':0,'Z':1}

P2TABLE = {'A':[1,2,3],
            'B':[2,3,1],
            'C':[3,1,2]}


def main(file):
    data = extract(file)
    Points = 0
    #PART 1
    for i in data:
        Points += VALUES[i[1]] + TABLE[i[0]][i[1]]
    print("Solution Part 1:%s" %(Points))
    #PART 2
    Points_2 = 0
    for i in data:
        Points_2 += P2OUTCOME[i[1]] + P2TABLE[i[0]][P2VAL[i[1]]]
    print("Solution Part 2:%s" %(Points_2))
    

    

if __name__ == "__main__":
    main(sys.argv[1])
