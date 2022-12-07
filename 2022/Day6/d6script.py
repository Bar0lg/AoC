import sys,os,time,math,copy
import numpy as np

import aoc_scripts as aoc

def extract(file):
    return open(file,'r').read()

def main(file):
    data = extract(file)
    n = len(data)
    i = 0
    #PART 1
    while True:
        a = data[i]
        b = data[i+1]
        c = data[i+2]
        d = data[i+3]
        if (a not in [b,c,d]) and (b not in [c,d]) and (c not in [d]):
            break
        i += 1
    print("Solution Part 1:%s" %(i+4))

    #PART 2
    for i in range(n-14):
        tab_1 = data[i:i+14]
        ens = aoc.create_ens(tab_1)
        if len(ens) == len(tab_1):
            res2 = i
            break
    print("Solution Part 2:%s" %(res2+14))


if __name__ == "__main__":
    main(sys.argv[1])
