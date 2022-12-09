import sys,os,time,math,copy
import numpy as np

import aoc_scripts as aoc


def extract(file):
    f = open(file,'r').read().split('\n')
    f = [i.split(' ') for i in f]
    return f

def poss_move(coord):
    res = []
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            res.append((coord[0]+i,coord[1]+j))
    return res

def move_point(coo1,mov):
    match mov:
        case 'R':
            return (coo1[0]+1,coo1[1])
        case 'U':
            return (coo1[0],coo1[1]+1)
        case 'L':
            return (coo1[0]-1,coo1[1])
        case 'D':
            return (coo1[0],coo1[1]-1)

def is_next_to(coo1,coo2):
    neib = poss_move(coo2)
    for i in neib:
        if i == coo1:
            return True
    return False




def move_p2(coo1,coo2):
    res = coo1
    UP = (0,2)
    LEFT = (-2,0)
    RIGHT = (2,0)
    DOWN = (0,-2)
    UR = aoc.create_spe_coo([2,1],[2,1],[(1,1)])
    UL = aoc.create_spe_coo([-2,-1],[2,1],[(-1,1)])
    DR = aoc.create_spe_coo([2,1],[-2,-1],[(1,-1)])
    DL = aoc.create_spe_coo([-2,-1],[-2,-1],[(-1,-1)])
    rela_coo = aoc.add_coo(coo2,(-coo1[0],-coo1[1]))
    
    if rela_coo == UP:
        res = move_point(coo1,'U')
    elif rela_coo == LEFT:
        res = move_point(coo1,'L')
    elif rela_coo == RIGHT:
        res = move_point(coo1,'R')
    elif rela_coo == DOWN:
        res = move_point(coo1,'D')
    elif rela_coo in UR:
        res = move_point(coo1,'U')
        res = move_point(res,'R')
    elif rela_coo in UL:
        res = move_point(coo1,'U')
        res = move_point(res,'L')
    elif rela_coo in DR:
        res = move_point(coo1,'D')
        res = move_point(res,'R')
    elif rela_coo in DL:
        res = move_point(coo1,'D')
        res = move_point(res,'L')
    else:
        print("ERREUR")
        print(rela_coo)
        print(coo1,coo2)
    return res


def main(file):
    ins = extract(file)
    visited = []
    coo_head = (0,0)
    coo_tail = (0,0)
    prev_place = (0,0)
    for i in ins:
        for step in range(int(i[1])):

            prev_place = coo_head
            coo_head = move_point(coo_head,i[0])
            if not is_next_to(coo_head,coo_tail):
                coo_tail = prev_place
            visited.append(coo_tail)
    visited = aoc.create_ens(visited)

    #PART 2
    visited_P2 = []
    coo_rope = [(0,0)]*10
    for i in ins:
        for step in range(int(i[1])):
            coo_rope[0] = move_point(coo_rope[0],i[0])
            for num_r in range(1,len(coo_rope)):
                if not is_next_to(coo_rope[num_r],coo_rope[num_r-1]):
                    coo_rope[num_r] = move_p2(coo_rope[num_r],coo_rope[num_r-1])
            visited_P2.append(coo_rope[-1])

    visited_P2 = aoc.create_ens(visited_P2)



    print("Solution Part 1:%s" %(len(visited)))
    print("Solution Part 2:%s" %(len(visited_P2)))



if __name__ == "__main__":
    main(sys.argv[1])
