import numpy as np
import sys,os,time,math,copy


xmin = 248 
xmax = 285
ymin = -85
ymax = -56
maxheight = 3570
def main():
	print("Testing started:")
	attempt = 0
	succes = 0
	for i  in range(0,xmax+1):
		for k in range(ymin,maxheight+1):
			probe = [0,0]
			xspeed = i
			yspeed = k
			while probe[0] <= xmax and probe[1] >= ymin:
				probe[0] += xspeed
				probe[1] += yspeed
				xspeed = max(0,xspeed -1)
				yspeed -= 1
				if xmin <= probe[0] <= xmax and ymax >= probe[1] >= ymin:
					succes += 1
					break
			attempt += 1
			print("Tested:%s	Hit:%s"%(attempt,succes),end="\r")
	print("\n")
main()

