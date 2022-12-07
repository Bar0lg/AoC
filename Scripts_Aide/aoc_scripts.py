import sys,os,time,math,copy
import numpy as np


def str_to_int_conv(list_to_conv):
    res = []
    for i in list_to_conv:
        if type(i) == list:
            res.append(str_to_int_conv(i))
        else:
            res.append(int(i))
    return res