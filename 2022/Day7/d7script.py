import sys,os,time,math,copy
import numpy as np

import aoc_scripts as aoc



def extract(file):
    return open(file,'r').read().split('\n')


class System:
    def __init__(self,parent,root):
        self.parent = parent
        self.files = {}
        self.dirs = {}
        self.root = root

    def mkdir(self,name):
        self.dirs[name] = System(self,self.root)
    
    def cd(self,name):
        match name:
            case '/':
                return self.root
            case '..':
                return self.parent
            case _ :
                return self.dirs[name]

    def touch(self,size,file_name):
        self.files[file_name] = size

    def tree_data(self,part):
        global p1_sol
        global p2_sol
        match part:
            case 2:
                res_files = sum([self.files[i] for i in self.files])
                res = res_files
                for i in self.dirs:
                    res += self.dirs[i].tree_data(2)
                p2_sol.append(res)
                return res
            case 1:
                res_files = sum([self.files[i] for i in self.files])
                res = res_files
                for i in self.dirs:
                    res += self.dirs[i].tree_data(1)
                if res <= 100000:
                    p1_sol += res 
                return res





def pattern_checker(ins):
    # 0 = cd command
    # 1 = ls command
    # 2 = dir command
    # 3 = file command
    if ins[0] == '$':
        if ins[2:4] == 'cd':
            return 0
        else:
            return 1
    else:
        if ins[0:3] == 'dir':
            return 2
        else:
            return 3


SYSTEM_SIZE = 70000000

NEED_FREE = 30000000

def main(file):
    global p1_sol
    global p2_sol
    p1_sol = 0
    p2_sol = []
    data = extract(file)
    pointer = System(None,None)
    pointer.root = pointer
    for i in data:
        match pattern_checker(i):
            case 0:
                pointer = pointer.cd(i[5:])
            case 1:
                pass
            case 2:
                pointer.mkdir(i[4:])
            case 3:
                file_info = i.split(' ')
                pointer.touch(int(file_info[0]),file_info[1])
            case _ :
                print("ERROR")
    pointer = pointer.cd('/')
    pointer.tree_data(1)
    print("Solution Part 1:%s" %(p1_sol))

    #Part 2
    pointer.tree_data(2)
    res = []
    for i in p2_sol:
        if i >= NEED_FREE - (SYSTEM_SIZE - (max(p2_sol))):
            res.append(i)
    print("Solution Part 2:%s" %(min(res)))

if __name__ == "__main__":
    main(sys.argv[1])
