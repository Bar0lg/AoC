import numpy as np
import sys,os,time,math,copy

def extract(file):
    f = open(file,"r")
    res = f.readline()[:-1].split(",")
    return res



def script(file,time):
    start = extract(file)
    tab = np.zeros(9,dtype=int)
    for i in start:
        iint = int(i)
        tab[iint] += 1
    print(tab)
    for i in range(1,time+1):
        new_lant = tab[0]
        for j in range(1,9):
            tab[j-1] = tab[j]
        tab[8] = new_lant
        tab[6] += new_lant
        print(tab.sum(),"       Jour %s"%(i))
    return tab





b = script("input",256)
print(b.sum())
