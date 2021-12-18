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
    top_bott_florr = np.ones(len(res[0])+2,dtype=int)*9
    left_and_right = (np.ones(len(res[:,1]),dtype=int)*9).reshape(len(res[:,1]),1)
    res = np.hstack((left_and_right,res))
    res = np.hstack((res,left_and_right))
    res = np.vstack((top_bott_florr,res))
    res = np.vstack((res,top_bott_florr))
    return res


def script1(file):
    tab = extract(file)
    list_low_points = []
    res = 0
    for i in range(1,len(tab[:,1])-1):
        for k in range(1,len(tab[1])-1):
            if tab[i][k] < tab[i+1][k] and tab[i][k] < tab[i-1][k] and tab[i][k] < tab[i][k+1] and tab[i][k] < tab[i][k-1]:
                list_low_points.append(tab[i][k])

    print(list_low_points)
    for i in list_low_points:
        res += i +1
    return res

visited = []
def recursize(tab,i,k):
    global visited
    if (i,k) in visited:
        return 0
    visited.append((i,k))
    if tab[i][k] == 9:
        return 0
    else:
        return 1 + recursize(tab,i+1,k) + recursize(tab,i-1,k) +recursize(tab,i,k+1) +recursize(tab,i,k-1)


def script2(file):
    tab = extract(file)
    Bassin_size = []
    res = 1
    global visited
    for i in range(1,len(tab[:,1])-1):
        for k in range(1,len(tab[1])-1):
            if (i,k) in visited:
                pass
            else:
                Bassin_size.append(recursize(tab,i,k))
    print(Bassin_size)
    Bassin_size.sort()
    for i in Bassin_size[-3:]:
        res *= i
    return res


print(script2("input"))
