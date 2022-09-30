import numpy as np
import sys,os,time,math,copy

def extract(file):
    f = open(file,"r")
    res = f.read()
    res = res.split("\n")
    for i in range(len(res)):
        res[i] = [j for j in res[i]]
    return res



def scan(data):
    couples = {"(":")","[":"]","{":"}","<":">"}
    opens   = ["(","[","{","<"]
    closes  = [")","]","}",">"]
    awaitw   = []
    for k in data:
        if k in opens:
            awaitw.append(couples[k])
            pass
        if k in closes:
            if k == awaitw[-1]:
                awaitw.pop(-1)
                pass
            else:
                return k
    return awaitw



def script1(file):
    data = extract(file)
    couples = {"(":")","[":"]","{":"}","<":">"}
    opens  = ["(","[","{","<"]
    closes = [")","]","}",">"]
    points = {")":1,"]":2,"}":3,">":4}
    Errors = []
    res = 0
    for i in data:
        Errors.append(scan(i))
    new_list = []
    for i in Errors:
        if type(i) == str:
            pass
        else:
            new_list.append(i)
    scrore_list = []
    new_list.pop(-1)
    for i in new_list:
        score = 0
        for k in range(len(i)-1,-1,-1):
            score = (score * 5) + points[i[k]]
        scrore_list.append(score)
    scrore_list.sort()
    print(scrore_list)

    return scrore_list[len(scrore_list)//2]



print(script1("input"))
