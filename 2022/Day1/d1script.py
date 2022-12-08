import sys,os,time,math,copy
import numpy as np

import aoc_scripts as aoc

def extract(file):
    f = open(file,"r").read().split("\n\n")
    data = [i.split("\n") for i in f]
    return data


        

def main(file):
    data = aoc.str_to_int_conv(extract(file)) 

    #Part 1
    Cal_per_elves = [sum(i) for i in data]
    print("Solution Part1:%s" %(max(Cal_per_elves)))
    #Part2
    Cal_per_elves.sort()
    print("Solution Part2:%s" %(Cal_per_elves[-1]+Cal_per_elves[-2]+Cal_per_elves[-3]))


if __name__ == "__main__":
    main(sys.argv[1])
