import sys,os,time,math,copy
import numpy as np

import aoc_scripts as aoc



def extract(file):
    f = open(file,'r').read().split('\n')
    f = [list(i) for i in f]
    f = aoc.str_to_int_conv(f)
    return np.array(f)


def is_exterior(x,y,xmax,ymax):
    return (x in [0,xmax]) or (y in [0,ymax])

def is_OOB(x,y,xmax,ymax):
    return (x in [-1,xmax+1]) or (y in [-1,ymax+1])




def is_visible(tab,x,y,direction,goal):
    if is_exterior(x,y,len(tab)-1,len(tab[0])-1):
        return True
    match direction:
        case 'north':
            if tab[x-1][y] >= goal:
                return False
            return True and is_visible(tab,x-1,y,'north',goal)


        case 'south':
            if tab[x+1][y] >= goal:
                return False
            return True and is_visible(tab,x+1,y,'south',goal)


        case 'east':
            if tab[x][y+1] >= goal:
                return False
            return True and is_visible(tab,x,y+1,'east',goal)


        case 'west':
            if tab[x][y-1] >= goal:
                return False
            return True and is_visible(tab,x,y-1,'west',goal)

def num_tree_visible(tab,x,y,direction,goal):
    if is_OOB(x,y,len(tab)-1,len(tab[0])-1):
        return 0
    match direction:
        case 'north':
            if is_OOB(x-1,y,len(tab)-1,len(tab[0])-1):
                return 0
            if tab[x-1][y] >= goal:
                return 1
            return 1 + num_tree_visible(tab,x-1,y,'north',goal)


        case 'south':
            if is_OOB(x+1,y,len(tab)-1,len(tab[0])-1):
                return 0
            if tab[x+1][y] >= goal:
                return 1
            return 1 + num_tree_visible(tab,x+1,y,'south',goal)


        case 'east':
            if is_OOB(x,y+1,len(tab)-1,len(tab[0])-1):
                return 0
            if tab[x][y+1] >= goal:
                return 1
            return 1 + num_tree_visible(tab,x,y+1,'east',goal)


        case 'west':
            if is_OOB(x,y-1,len(tab)-1,len(tab[0])-1):
                return 0
            if tab[x][y-1] >= goal:
                return 1
            return 1 + num_tree_visible(tab,x,y-1,'west',goal)




def main(file):
    tab = extract(file)
    xmax = len(tab)
    ymax = len(tab[0])
    res1 = 0
    res2 = []
    for x in range(xmax):
        for y in range(ymax):
            tree = tab[x][y]

            visible = is_visible(tab,x,y,'north',tree) or is_visible(tab,x,y,'south',tree) or is_visible(tab,x,y,'east',tree) or is_visible(tab,x,y,'west',tree)

            visibles_tree = num_tree_visible(tab,x,y,'north',tree) * num_tree_visible(tab,x,y,'south',tree) *num_tree_visible(tab,x,y,'east',tree) *num_tree_visible(tab,x,y,'west',tree)

            if visible:
                res1 += 1
            res2.append(visibles_tree)
    print("Solution Part 1:%s" %(res1))
    print("Solution Part 2:%s" %(max(res2)))    

if __name__ == "__main__":
    main(sys.argv[1])
