import numpy as np
import sys,os,time,math,copy


def extract(file):
    f = open(file,"r")
    res = (f.read().split("\n"))
    res.pop(-1)
    for i in range(len(res)):
        res[i] = res[i].split("|")
        res[i][0] = res[i][0].split()
        res[i][1] = res[i][1].split()
    res = np.array(res,dtype=object)
    return res

def script1(file):
    data = extract(file)
    res = 0
    for i in data:
        for j in i[1]:
            if len(j) in [2,3,4,7]:
                res += 1
    return res

def translate(id,k):
    for i in id:
        if sorted(i) == sorted(k):
            return id[i]


def filter_by_count(list,num):
    res = []
    for i in list:
        if len(i) == num:
            res.append(i)
    return res


def find_one(list):
    for i in list:
        if len(i) == 2:
            return i
    print("ERROR")
    return False



def find_seven(list):
    for i in list:
        if len(i) == 3:
            return i
    print("ERROR")
    return False




def find_four(list):
    for i in list:
        if len(i) == 4:
            return i
    print("ERROR")
    return False



def find_eight(list):
    for i in list:
        if len(i) == 7:
            return i
    print("ERROR")
    return False

def find_nine(list,four):
    for i in list:
        num_di = 0
        for k in i:
            if k in four:
                num_di += 1
        if num_di == 4:
            return i



def find_three(list,seven):
    for i in list:
        num_di = 0
        for k in i:
            if k in seven:
                num_di += 1
        if num_di == 3:
            return i


def find_upbar(seven,four):
    for i in seven:
        if i not in four:
            return i


def find_two_and_five(list,four,three):
    list.remove(three)
    for i in list:
        num_di = 0
        for k in i:
            if k in four:
                num_di += 1
        if num_di == 2:
            two = i
    list.remove(two)
    return two , list[0]


def find_six_and_zero(list,five,nine):
    list.remove(nine)
    for i in list:
        num_di = 0
        for k in i:
            if k in five:
                num_di += 1
        if num_di == 5:
            six = i
    list.remove(six)
    return six , list[0]


def script2(file):
    data = extract(file)
    res = 0
    for i in data:
        one   = find_one(i[0])
        seven = find_seven(i[0])
        four  = find_four(i[0])
        eight = find_eight(i[0])
        nine  = find_nine(filter_by_count(i[0],6),four)
        three = find_three(filter_by_count(i[0],5),seven)
        up_bar = find_upbar(seven,four)
        two , five = find_two_and_five(filter_by_count(i[0],5),four,three)
        six , zero = find_six_and_zero(filter_by_count(i[0],6),five,nine)
        print(one,seven,four,eight,nine,three,two,five,six,zero)
        id = {
        zero:'0',
        one:'1',
        two:'2',
        three:'3',
        four:'4',
        five:'5',
        six:'6',
        seven:'7',
        eight:'8',
        nine:'9'
        }
        res_temp = ''
        for k in i[1]:
            res_temp += translate(id,k)

        res += int(res_temp)
    return res
print(script2("input"))
