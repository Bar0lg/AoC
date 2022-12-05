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


# Liste de int --> Liste de str
def int_to_str_conv(list_to_conv):
    res = []
    for i in list_to_conv:
        if type(i) == list:
            res.append(int_to_str_conv(i))
        else:
            res.append(str(i))
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

def clean_str(string,elemes,option=0):
    res = ''
    for i in string:
        if i not in elemes:
            res += i
    return res
            


def clean_tab (tab,elemes,option=0):
    res = []
    for i in tab:
        if type(i) == list:
            res.append(clean_tab(i, elemes,option))
        else:
            if not option:
                if i not in elemes:
                    res.append(i)
            else:
                if i in elemes:
                    res.append(i)
    return res




def clean_all_but_int(stri):

    num = int_to_str_conv(range(10))
    res = ''
    for i in stri:
        if i in num or i == ' ':
            res += i
    rres = ''
    for i in range(len(res)):
        if i == len(res)-1 or i == 0:
            if res[i] == ' ':
                pass
            else:
                rres += res[i]
        else:
            if res[i] == ' ' and res[i+1] == ' ':
                pass
            else:
                rres += res[i]
    return rres


def concat_list(tab):
    res = ''
    for i in tab:
        res += i
    return res