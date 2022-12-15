import sys,os,time,math,copy
import numpy as np

import aoc_scripts as aoc

def create_file(file):
    f = open(file,'r').read().split('\n\n')
    f = aoc.deep_split(f,'\n')

    new_file = open('Input_parsed.py','w')
    new_file.write('DATA = [')
    for couple in range(len(f)):
        new_file.write('[')
        new_file.write(f[couple][0])
        new_file.write(', ')
        new_file.write(f[couple][1])
        if couple == len(f)-1:
            new_file.write(']')
        else:
            new_file.write('], ')
    new_file.write('] ')

    new_file.close()


def comp_lists(list1,list2):
    if type(list1) == int and type(list2) == int:
        if list1 == list2:
            return 'Tie'
        if list1 < list2:
            return True
        return False
    
    if type(list1) == int and type(list2) == list:
        return comp_lists([list1],list2)

    if type(list1) == list and type(list2) == int:
        return comp_lists(list1,[list2])

    if type(list1) == list and type(list2) == list:
        #print(list1,list2)
        for slot in range(max(len(list1),len(list2))):
            if slot == len(list1) and slot == len(list2):
                return 'Tie'
            if slot == len(list1):
                return True
            if slot == len(list2):
                return False
            res = comp_lists(list1[slot],list2[slot])
            if res != 'Tie':
                return res
        return 'Tie'
                



def main(file):
    create_file(file)
    from Input_parsed import DATA
    #print(DATA)
    res1 = 0
    res22 = 1
    res26 = 2 #bc [[2]] < [[6]]
    for couple in range(len(DATA)):
        if comp_lists(DATA[couple][0],DATA[couple][1]):
            #print(couple+1)
            res1 += couple +1
        if comp_lists(DATA[couple][0],[[2]]):
            res22 += 1
        if comp_lists(DATA[couple][0],[[6]]):
            res26 += 1
        if comp_lists(DATA[couple][1],[[2]]):
            res22 += 1
        if comp_lists(DATA[couple][1],[[6]]):
            res26 += 1
        
    #print(res22,res26)
    print("Solution Part 1:%s" %(res1))
    print("Solution Part 2:%s" %(res22 * res26))



if __name__ == "__main__":
    main(sys.argv[1])
