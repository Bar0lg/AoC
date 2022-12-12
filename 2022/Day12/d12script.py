import sys,os,time,math,copy
import numpy as np

import aoc_scripts as aoc

HEIGHT = list('SabcdefghijklmnopqrstuvwxyzE')

def extract(file):
    f = open(file,'r').read().split('\n')
    f = [list(i) for i in f]
    return f


def find_nei(tab,i,j,ni,nj):
    if ni >= len(tab) or ni < 0:
        return 'NOPE'
    if nj >= len(tab[0]) or nj < 0:
        return 'NOPE'
    #print(HEIGHT.index(tab[ni][nj]),HEIGHT.index(tab[i][j])+1,(ni,nj),(i,j))
    if HEIGHT.index(tab[ni][nj]) <= HEIGHT.index(tab[i][j])+1:
        #print('passed')
        return (ni,nj)
    #print('fail')
    return 'NOPE'

def main(file,part):
    turn = 0
    map_data = extract(file)
    visited = []
    dist_tab = [[math.inf]*len(map_data[0]) for i in range(len(map_data))]

    to_visit = []
    
    strtcoos = aoc.find_in_2D_grid(map_data,'S')

    if part == '2':
        strtcoos += aoc.find_in_2D_grid(map_data,'a')

    for start in strtcoos:
        dist_tab[start[0]][start[1]] = 0
        to_visit.append(start)



    endcoos = aoc.find_in_2D_grid(map_data,'E')


    #Dijkastra
    print('Begin Dijkastra...')
    while endcoos[0] not in visited:
        #Find lowest
        low_val = math.inf
        low_i ,low_j = 0,0


        for i in to_visit:
            cooi,cooj = i[0],i[1] 
            if dist_tab[cooi][cooj] < low_val and i not in visited:
                low_i,low_j = cooi,cooj
                low_val = dist_tab[cooi][cooj]

        #Find nei
        nei = []
        nei.append(find_nei(map_data,low_i,low_j,low_i+1,low_j))
        nei.append(find_nei(map_data,low_i,low_j,low_i-1,low_j))
        nei.append(find_nei(map_data,low_i,low_j,low_i,low_j+1))
        nei.append(find_nei(map_data,low_i,low_j,low_i,low_j-1))
        
        cleaned_nei = []
        for i in nei:
            if i != 'NOPE'and i not in visited:
                cleaned_nei.append(i)
                to_visit.append(i)
        nei = cleaned_nei

        to_visit = aoc.create_ens(to_visit)



        #setting value for nei
        for i in nei:
            #print(i)
            if dist_tab[low_i][low_j] + 1 < dist_tab[i[0]][i[1]]:
                dist_tab[i[0]][i[1]] = dist_tab[low_i][low_j] + 1


        
        visited.append((low_i,low_j))
        #print((low_i,low_j))
        to_visit.remove((low_i,low_j))
        #print(to_visit)
        
        
    print("\n\nSolution Part %s:%s" %(part,dist_tab[endcoos[0][0]][endcoos[0][1]]))
                 

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])
