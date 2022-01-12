import numpy as np
import sys,os,time,math,copy

sumver = 0

hextable = {
"0" : "0000" ,
"1" : "0001" ,
"2" : "0010" ,
"3" : "0011" ,
"4" : "0100" ,
"5" : "0101" ,
"6" : "0110" ,
"7" : "0111" ,
"8" : "1000" ,
"9" : "1001" ,
"A" : "1010" ,
"B" : "1011" ,
"C" : "1100" ,
"D" : "1101" ,
"E" : "1110" ,
"F" : "1111"
}

def extract(file):
	f=open(file,"r")
	return f.read()	
def bytetonumber(byte):
	res = 0
	power = 1
	for i in range(len(byte)-1,-1,-1):
		res = int(byte[i])*power + res
		power *= 2
	return res

def hextostring(hexa):
	res = ""
	for i in hexa:
		res = res + hextable[i]
	return res

def type4decrypt(byte):
	res = ""
	x = 0
	y = 5
	while True:
		res = res + byte[x+1:y]
		if byte[x] == "0":
			break
		x += 5
		y += 5
	return int(res,2),y+6

def headerID(byte):
	ver = bytetonumber(byte[:3])
	PaID = bytetonumber(byte[3:6])
	return ver,str(PaID)

def lenghtID(byte):
	if byte[0] == "0":
		length = bytetonumber(byte[1:16])
	else:
		length = bytetonumber(byte[1:12])
	return length , byte[0]

def script1(byte,lengh0=-1):
	res = 0
	if bytetonumber(byte) == 0:
		return 0
	global sumver
	ver,PaID = headerID(byte)
	sumver += ver
	if PaID == "4":
		print("num")
		print(type4decrypt(byte[6:]))
		return type4decrypt(byte[6:])
	else:
		tests = []
		length,LeID = lenghtID(byte[6:])
		print(length,LeID)
		if LeID == "0":
			y = 0
			print("sub")
			while length != 0:
				number , ytoadd = script1(byte[22+y:])
				tests.append(number)
				length -= ytoadd		
				y += ytoadd
			if PaID == "0":
				res = 0
				for i in tests:
					res += i
			if PaID == "1":
				res = 1
				for i in tests:
					res *= i
			if PaID == "2":
				res = min(tests)
			if PaID == "3":
				res = max(tests)
			if PaID == "5":
				if tests[0] > tests[1]:
					res = 1
				else:
					res = 0
			if PaID == "6":
				if tests[0] < tests[1]:
					res = 1
				else:
					res = 0
			if PaID == "7":
				if tests[0] == tests[1]:
					res = 1
				else:
					res = 0

			print(res,tests)
			return res,y+22
		if LeID == "1":
			y=0
			print("sub2")
			while length != 0:
				number , ytoadd = script1(byte[18+y:])
				tests.append(number)
				length -= 1		
				y += ytoadd
			if PaID == "0":
				res = 0
				for i in tests:
					res += i
			if PaID == "1":
				res = 1
				for i in tests:
					res *= i
			if PaID == "2":
				res = min(tests)
			if PaID == "3":
				res = max(tests)
			if PaID == "5":
				if tests[0] > tests[1]:
					res = 1
				else:
					res = 0
			if PaID == "6":
				if tests[0] < tests[1]:
					res = 1
				else:
					res = 0
			if PaID == "7":
				if tests[0] == tests[1]:
					res = 1
				else:
					res = 0
			print(res,tests)
			return res,y+18


file = hextostring(extract("RealInput17.txt")[:-1])
#file = hextostring("9C0141080250320F1802104A08")
print(script1(file))
print(sumver)
