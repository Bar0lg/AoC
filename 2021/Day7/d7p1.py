import numpy as np
import sys,os,time,math,copy

def extract(file):
    f = open(file,"r")
    res = (f.readline()[:-1].split(","))
    res = list(map(int,res))
    res = np.array(res)
    return res


def script(file):
    data = extract(file)
    max = np.max(data)
    min = np.min(data)
    print(min,max)
    res = math.inf
    for i in range(min,max+1):
        temp_res = 0
        for k in data:
            n = abs(i-k)
            temp_res += (n*(n+1))//2
        if temp_res < res:
            res = temp_res
    return res

print(script("input"))
