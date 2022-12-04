import sys,os,time,math,copy
import numpy as np

# Liste de str --> Liste de int
def str_to_int_conv(list_to_conv):
    res = []
    for i in list_to_conv:
        if type(i) == list:
            res.append(str_to_int_conv(i))
        else:
            res.append(int(i))
    return res

def is_in(tab1,tab2,option=0):
    #option 0 --> ALL tab1 is in tab2
    #option 1 --> At least 1 of tab1 is in tab2 
    #tab 1 in tab 2
    if not option:
        for i in tab1:
            if i not in tab2:
                return False
        return True
    else:
        for i in tab1:
            if i in tab2:
                return True
        return False
