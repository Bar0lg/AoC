import sys,os,time,math,copy
import numpy as np

import aoc_scripts as aoc

def extract(file):
    f = open(file,'r').read().split('\n')
    print_file = open('printfile.txt','w')
    data = [i.split('->') for i in f]
    data = aoc.str_to_int_conv(aoc.deep_split(data,','))
    return data
    
    
    
#rocks (y,x)

def main(file,part):
    data = extract(file)
    all_rocks = []
    for i in data:
        all_rocks += i
    #print(all_rocks)
    x_max_p2 = max([i[1] for i in all_rocks]) + 2
    if part == '2':
        data.append([[0,x_max_p2],[1000,x_max_p2]])
    rocks = []
    #print(data)
    for struct in data:
        for num_wall in range(len(struct)-1):
            start = struct[num_wall]
            dest = struct[num_wall+1]
            if start[0] == dest[0]: #Same y axis
                diff = dest[1] - start[1]
                rock_to_place = (start[0],start[1])
                rocks.append(rock_to_place)
                while rock_to_place != (dest[0],dest[1]):
                    if diff > 0:
                        rock_to_place = (rock_to_place[0],rock_to_place[1]+1)
                    else:
                        rock_to_place = (rock_to_place[0],rock_to_place[1]-1)
                    rocks.append(rock_to_place)
            
            if start[1] == dest[1]: #Same x axis
                diff = dest[0] - start[0]
                rock_to_place = (start[0],start[1])
                rocks.append(rock_to_place)
                while rock_to_place != (dest[0],dest[1]):
                    if diff > 0:
                        rock_to_place = (rock_to_place[0]+1,rock_to_place[1])
                    else:
                        rock_to_place = (rock_to_place[0]-1,rock_to_place[1])
                    rocks.append(rock_to_place)
                
    rocks = aoc.create_ens(rocks)
    x_max = max(i[1]for i in rocks)+2

    dict_rocks = {}
    for rock in rocks:
        if rock[0] not in dict_rocks:
            dict_rocks[rock[0]] = {}
        dict_rocks[rock[0]][rock[1]] = True
    res = 0
    while True:
        dict_copy = copy.deepcopy(dict_rocks)
        sand = (500,0)
        while True:
            if sand[0] not in dict_rocks:
                break
            if sand[1]+1 not in dict_rocks[sand[0]]:
                sand = (sand[0],sand[1]+1)
                continue
            if sand[0]-1 not in dict_rocks:
                sand = (sand[0]-1,sand[1]+1)
                continue
            if sand[1]+1 not in dict_rocks[sand[0]-1]:
                sand = (sand[0]-1,sand[1]+1)
                continue


            if sand[0]+1 not in dict_rocks:
                sand = (sand[0]+1,sand[1]+1)
                continue
            if sand[1]+1 not in dict_rocks[sand[0]+1]:
                sand = (sand[0]+1,sand[1]+1)
                continue
            break
        if sand[0] not in dict_rocks: #Part 1 cond
            break
        if sand[1] in dict_rocks[sand[0]]: #Part 2 cond
            break
        res += 1
        
        dict_rocks[sand[0]][sand[1]] = True
        #aoc.comp_dict(dict_rocks,dict_copy)
        #input()
    
    print("Solution Part %s:%s" %(part,res))
        

                


    

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])
