import sys,os,time,math,copy
import numpy as np

PRIO = [i for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']


def extract(file):
    return open(file,'r').read().split('\n')

def main(file):
    data = extract(file)
    #Part 1
    resp1 = 0
    for i in data:
        half = len(i) // 2
        firsthalf , sechalf = i[:half] , i[half:]
        for j in firsthalf:
            if j in sechalf:
                resp1 += PRIO.index(j) + 1
                break
    print("Solution Part 1:%s"%(resp1))

    #Part 2
    resp2 = 0
    for i in range(0,len(data),3):
        for j in data[i]:
            if j in data[i+1] and j in data[i+2]:
                resp2 += PRIO.index(j) + 1
                break
    print("Solution Part 2:%s"%(resp2))

if __name__ == "__main__":
    main(sys.argv[1])
