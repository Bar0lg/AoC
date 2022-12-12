import sys,os,time,math,copy
import numpy as np

import aoc_scripts as aoc

def extract(file):
    f = open(file,'r').read().split('\n\n')
    f = aoc.deep_split(f,'\n')
    f = [i[1:] for i in f]
    # 0 = *
    # 1 = +
    for i in range(len(f)):
        ope = aoc.clean_tab(f[i][1],['*','+'],1)
        if ope == ['+']:
            f[i].append('1')
        else:
            f[i].append('0')

        f[i][0] = f[i][0].split(' ')
    f = aoc.deep_command(f, aoc.clean_all_but_int)
    f = aoc.clean_tab(f,[''])
    f = aoc.str_to_int_conv(f)
    return f


"""
    Table:
        f[i] = Num of Monkey
        f[i][0] = List of obj
        f[i][1] = num who must be [ope] by old !!! if len(f[i]) != 6 its    old [ope] old
        f[i][2] = Test whis must be divisible
        f[i][3] = Monkey in case of success
        f[i][4] = Monkey in case of failure
        f[i][5] = [ope] + if 1      * if 0 
"""

class Monkey:
    def __init__(self,obj,num_to_ope,test_num,success,failure,ope):
        self.obj = obj
        self.num_to_ope = num_to_ope
        self.test_num = test_num
        self.success = success
        self.failure = failure
        self.ope = ope
        self.num_inspected = 0

    def clean_obj(self):
        self.obj = []


    def ex_ope(self,obj,part,modul):
        self.num_inspected += 1
        if part == 1:
            if self.num_to_ope == -1:
                return (obj * obj)//3
            if self.ope == 0:
                return (obj * self.num_to_ope)//3
            else:
                return (obj + self.num_to_ope)//3
        else:
            if self.num_to_ope == -1:
                return (obj * obj) % modul
            if self.ope == 0:
                return (obj * self.num_to_ope) % modul
            else:
                return (obj + self.num_to_ope) % modul

    def check_cond(self,val):
        if val % self.test_num == 0:
            return self.success
        return self.failure


def main(file,num_turn,part):
    num_turn = int(num_turn)
    initdata = extract(file)
    monkeys = []
    modul_p2 = 1
    for i in initdata:

        if len(i) != 6:
            monkeys.append(Monkey(i[0],-1,i[1],i[2],i[3],i[4]))
            modul_p2 *= i[1]
        else:
            monkeys.append(Monkey(i[0],i[1],i[2],i[3],i[4],i[5]))
            modul_p2 *= i[2]

    for turn in range(num_turn):
        for i in range(len(monkeys)):
            for obj in monkeys[i].obj:
                new_val = monkeys[i].ex_ope(obj,part,modul_p2)
                #print(new_val)
                monk_to_send = monkeys[i].check_cond(new_val)
                monkeys[monk_to_send].obj.append(new_val)
            monkeys[i].clean_obj()
        #print('%s---------------'%(turn))
        for i in range(len(monkeys)):
            #print('%s:%s'%(i,monkeys[i].obj))
            pass
            
            
    res = []
    for monk in monkeys:
        res.append(monk.num_inspected)
    
    res.sort()
    print(res)
    r1 , r2 = res[-1],res[-2]

    print("\n\nSolution Part %s:%s" %(part,r1*r2))
                


    


if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3])
