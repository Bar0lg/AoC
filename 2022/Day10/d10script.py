import sys,os,time,math,copy
import numpy as np

import aoc_scripts as aoc

def extract(file):
    f = open(file,'r').read().split('\n')
    f = [i.split(' ') for i in f]
    return f

def check_clock(clock,x):
    if (clock) % 40 == 0:
        print('\n',end='')
    if (clock) % 40 in [x-1,x,x+1]:
        print('#',end='')
    else:
        print('.',end='')
    #print(x ,clock)
    if (clock-20) % 40 == 0:
        return clock * x
    
    return 0

def main(file):
    res = []
    x = 1
    clock = -1
    ins = extract(file)
    print("\n\nSolution Part 2:")
    for i in ins:
        if i[0] == 'noop':
            clock += 1
            res.append(check_clock(clock,x))
        else:
            clock += 1
            res.append(check_clock(clock,x))

            clock +=1
            res.append(check_clock(clock,x))
            x += int(i[1])
            
    res = aoc.clean_tab(res,[0])
    print("\n\nSolution Part 1:%s" %(sum(res)))

if __name__ == "__main__":
    main(sys.argv[1])
