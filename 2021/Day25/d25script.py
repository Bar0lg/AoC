import sys,os,time,math,copy
import numpy as np

def extract(file):
    f = open(file,"r")
    data = f.read().split("\n")[:-1]
    data = [list(i) for i in data]
    #[print("%s\n"%(i)) for i in data]

    return data




def main(file):
    n = 0
    current_grid = extract(file)
    line = ['.']*len(current_grid[0])
    next_grid = []
    [next_grid.append(copy.deepcopy(line)) for i in range(len(current_grid))]
    clean_grid = copy.deepcopy(next_grid)
    imax = len(current_grid)
    jmax = len(current_grid[0])
    old_grid = None
    while current_grid != old_grid:
        for i in range(imax):
            for j in range(jmax):
                if current_grid[i][j] == '>':
                    moved = False
                    if j == jmax-1:
                        if current_grid[i][0] == ".":
                            moved = True
                            next_grid[i][0] = '>'
                    elif current_grid[i][j+1] == ".":
                        moved = True
                        next_grid[i][j+1] = '>'
                    if not moved:
                        next_grid[i][j] = '>'

                    
        for i in range(imax-1,-1,-1):
            for j in range(jmax-1,-1,-1):
                if current_grid[i][j] == 'v':
                    moved = False
                    if i == imax-1:
                        if (current_grid[0][j] == "." or current_grid[0][j] == ">") and (next_grid[0][j] != '>') :
                            moved = True
                            next_grid[0][j] = 'v'
                    elif (current_grid[i+1][j] == "." or current_grid[i+1][j] == ">") and (next_grid[i+1][j] != '>') :
                        moved = True
                        next_grid[i+1][j] = 'v'
                    if not moved:
                        next_grid[i][j] = 'v'
        #[print("STEP:%s  %s\n"%(i,n)) for i in next_grid]
        old_grid = copy.deepcopy(current_grid)
        current_grid = copy.deepcopy(next_grid)
        next_grid = copy.deepcopy(clean_grid)

        n += 1
    print(n)
if __name__ == "__main__":
    main(sys.argv[1])
