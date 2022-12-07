import sys,os,time,math,copy
import numpy as np

def export(file):
    f = open(file,"r")
    data0 = f.read().split("\n")[:-1]
    data1 = [i.split(" ") for i in data0]
    print(data1)

def main(file):
    ins = export(file)

if __name__ == "__main__":
    main(sys.argv[1])
