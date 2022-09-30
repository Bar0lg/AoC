import numpy as np
import sys,os,time,math,copy

def extract(file):
    f = open(file,"r")
    res = f.read().split("\n")
    res.pop(-1)
    dict = {}
    for i in range(len(res)):
        res[i] = res[i].split('-')
    for i in range(len(res)):
        if res[i][0] not in dict:
            dict[res[i][0]] = []
        if res[i][1] not in dict:
            dict[res[i][1]] = []
        dict[res[i][0]] += [res[i][1]]
        dict[res[i][1]] += [res[i][0]]
    return dict



Allpath = []
def recurpath(map,path,part2):
    global Allpath
    LocalPath = []
    #print(map)
    if path[-1] == 'end':
        return path
    for i in map[path[-1]]:
        if i == 'start':
            continue
        if i.islower() and i in path and part2 == True:
            LocalPath.append(recurpath(map,path+[i],False))
        if i.islower() and i in path:
            continue
        if path == ['start']:
             Allpath.append(recurpath(map,path+[i],part2))
        else:
            LocalPath.append(recurpath(map,path+[i],part2))
    if path == ['start']:
        return Allpath
    else:
        return LocalPath

Allist = []
def recurnested(list):
    global Allist
    if len(list) >= 1:
        if list[0] == 'start':
            Allist.append(list)
        else:
            for i in list:
                recurnested(i)

f = extract('Input')
res = recurpath(f,['start'],True)
recurnested(res)
print(len(Allist))
