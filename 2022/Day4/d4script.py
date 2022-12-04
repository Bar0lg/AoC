import sys,os,time,math,copy
import numpy as np
import aoc_scripts as aoc

def extract(file):
    f = open(file,'r').read().split("\n")
    f = [i.split(',') for i in f]
    f = [[i.split('-') for i in k] for k in f]
    f = aoc.str_to_int_conv(f)
    return f


def main(file):
    data = extract(file)
    #PART 1 and 2
    res1 = 0
    res2 = 0
    for i in data:
        assign1, assign2 = i[0] , i[1]
        r1 = range(assign1[0],assign1[1]+1)
        r2 = range(assign2[0],assign2[1]+1)
        if aoc.is_in(r1,r2):
            res1 +=1
        elif aoc.is_in(r2,r1):
            res1 += 1
        if aoc.is_in(r1,r2,1):
            res2 +=1
        elif aoc.is_in(r2,r1,1):
            res2 += 1
        
    print("Solution Part 1:%s" %(res1))
    print("Solution Part 2:%s" %(res2))
if __name__ == "__main__":
    main(sys.argv[1])
