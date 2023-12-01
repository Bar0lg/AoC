import sys,os,time,math,copy
import numpy as np

import aoc_scripts as aoc

sys. setrecursionlimit(100000000)

def extract(file):
    f = open(file,'r').read().split('\n')

    f = aoc.deep_split(f,':')
    f = aoc.deep_command(f,aoc.clean_all_but_int)
    f = aoc.deep_split(f,' ')
    f = aoc.clean_tab(f,[''])
    f = aoc.str_to_int_conv(f)
    return f


def calc_manat(coo1,coo2):
    #print(coo1,coo2)
    return abs(coo1[0]-coo2[0]) + abs(coo1[1]-coo2[1])

def main(file):
    data = extract(file)
    list_beacons = aoc.create_ens([i[1] for i in data])
    list_scans_and_man = [[i[0],calc_manat(i[0],i[1])] for i in data]
    list_scans = [i[0] for i in list_scans_and_man]
    res1 = 0
    #tst = []
    """
    for i in range(-1000000,10000000):
        p = [i,2000000]
        if p in list_scans or p in list_beacons:
            pass
        else:
            for scanners in list_scans_and_man:
                #print(p,scanners)
                #print(calc_manat(p,scanners[0]),scanners[1],calc_manat(p,scanners[0]) <= scanners[1])
                if calc_manat(p,scanners[0]) <= scanners[1]:
                    #tst.append(p)
                    res1 += 1
                    break
    print("Solution Part 1:%s" %(res1))
    """
    
    #print(tst)
    

if __name__ == "__main__":
    main(sys.argv[1])
