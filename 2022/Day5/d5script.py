import sys,os,time,math,copy
import numpy as np

import aoc_scripts as aoc

def extract(file):
    f= open(file,'r').read().split('\n\n')
    towers , ins = f[0] , f[1].split('\n')
    #Nb of towers
    nbtow = len(towers.split('\n')[-1].split('   '))
    tow_par = [[] for i in range(nbtow)]
    tow_sliced = towers.split('\n')
    for i in range(nbtow-1,-1,-1):
        stage = [tow_sliced[i][k] for k in range(1,len(tow_sliced[i]),4)]
        for k in range(len(stage)):
            tow_par[k].append((stage[k]))
    tow_par = aoc.clean_tab(tow_par,[' '])
    ins_par = [aoc.clean_all_but_int(i).split(' ') for i in ins]

    return tow_par ,ins_par

def main(file):
    tow,ins = extract(file)
    ins = aoc.str_to_int_conv(ins)
    tow2 = copy.deepcopy(tow[:])
    #PART 1
    for i in ins:
        for k in range(i[0]):
            crate = tow[i[1]-1].pop(-1)
            tow[i[2]-1].append(crate)
    #PART 2

    for i in ins:
        n = len(tow2[i[1]-1])
        crate = tow2[i[1]-1][n-i[0]:]
        for k in range(i[0]):
            tow2[i[1]-1].pop(-1)
        tow2[i[2]-1] += crate

    res1 = aoc.concat_list([i[-1] for i in tow ])
    res2 = aoc.concat_list([i[-1] for i in tow2])


    print("Solution Part 1:%s" %(res1))
    print("Solution Part 2:%s" %(res2))


if __name__ == "__main__":
    main(sys.argv[1])
