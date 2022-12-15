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
    """
    0 = Remove elmes
    1 = Remove ALL but elemes
    """
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



def create_ens(tab):
    res = []
    for i in tab:
        if i not in res:
            res.append(i)
    return res


def print_dicts(dict):
    for i in dict:
        print('%s : %s'%(i,dict[i]))

def print_grid(xmin,ymin,xmax,ymax,tab):
    print('\n')
    for y in range(ymin,ymax+1):
        for x in range(xmin,xmax+1):
            if (x,y) == (0,0):
                print('S',end='')
            elif (x,-y) in tab:
                print('X',end='')
            else:
                print('.',end='')
        print('\n')


def create_spe_coo(tab1,tab2,banned=[]):
    res = []
    for i in tab1:
        for j in tab2:
            if (i,j) not in banned:
                res.append(((i,j)))
    return res

def add_coo(coo1,coo2):
    return (coo1[0] + coo2[0],coo1[1] + coo2[1])


def deep_split(tab,spliter):
    res = []
    for i in tab:
        if type(i) == list:
            res.append(deep_split(i,spliter))
        else:
            res.append(i.split(spliter))
    return res


def deep_command(tab,command):
    res = []
    for i in tab:
        if type(i) == list:
            res.append(deep_command(i,command))
        else:
            res.append(command(i))
    return res


def find_in_2D_grid(tab,elem):
    res = []
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == elem:
                res.append((i,j))
    return res

def flat_list(tab):
    res = []
    for i in tab:
        if isinstance(i,list):
            res += flat_list(i)
        else:
            res += [i]
    return res

def cut_list(tab,min_x,max_x,min_y,max_y):
    res = [tab[i][min_y:max_y] for i in range(min_x,max_x)]
    return res

def comp_dict(dict1,dict2):
    for i in dict1:
        for k in dict1[i]:
            if k not in dict2[i]:
                print(i,k)
