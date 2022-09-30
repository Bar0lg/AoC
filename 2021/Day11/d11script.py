import numpy as np
import sys,os,time,math,copy

def extract(file):
    f = open(file,"r")
    res = f.read()
    res = res.split("\n")
    res.pop(-1)
    for i in range(len(res)):
        res[i] = [int(j) for j in res[i]]
    res = np.array(res,dtype=int)
    top_bott_florr = np.ones(12,dtype=int)*(-math.inf)
    left_and_right = (np.ones(10,dtype=int)*(-math.inf)).reshape(10,1)
    res = np.hstack((left_and_right,res))
    res = np.hstack((res,left_and_right))
    res = np.vstack((top_bott_florr,res))
    res = np.vstack((res,top_bott_florr))
    return res

def script(file,step):
    tab = extract(file)
    flash = 0
    for i in range(step):
        flashed = []
        tab= tab[:]+1
        no_flash = False
        while no_flash == False:
            no_flash = True
            for j in range(1,11):
                for k in range(1,11):
                    if tab[j][k] > 9:
                        if (j,k) not in flashed:
                            flashed.append((j,k))
                            no_flash = False
                            flash += 1
                            tab[j+1][k] = tab[j+1][k] +1
                            tab[j-1][k] = tab[j-1][k] +1
                            tab[j][k+1] = tab[j][k+1] +1
                            tab[j][k-1] = tab[j][k-1] +1
                            tab[j+1][k+1] = tab[j+1][k+1] +1
                            tab[j-1][k-1] = tab[j-1][k-1] +1
                            tab[j+1][k-1] = tab[j+1][k-1] +1
                            tab[j-1][k+1] = tab[j-1][k+1] +1
        for j in range(1,11):
            for k in range(1,11):
                if tab[j][k] > 9:
                    tab[j][k] = 0
        if len(flashed) == 100:
            print("All flashed at step : %s"%(i+1))
    print(flash)

script("input",500)
