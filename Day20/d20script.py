import sys,os
import numpy as np
def recupfile(file):
    f = open(file,'r').read()
    algo , image = f.split("\n\n")[0] , f.split("\n\n")[1]
    image = [[i.split() for i in k]for k in image.split("\n")]
    image.pop(-1)
    return algo,image

neighbors = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1))

def createborder(Image,lit):
    if lit % 2 == 0:
        k = '.'
    else:
        k = '#'
    walls = np.array([k]*len(Image)).reshape(-1,1)
    Image_Copy = np.hstack((walls,Image))
    Image_Copy = np.hstack((Image_Copy,walls))
    floor = np.array([k]*len(Image_Copy[0])).reshape(1,-1)
    Image_Copy = np.vstack((floor,Image_Copy))
    Image_Copy = np.vstack((Image_Copy,floor))
    return Image_Copy




def script(file,n):
    Algo,Image = recupfile(file)
    OldImage = np.array(Image).reshape(len(Image[0]),len(Image))
    Iter = 0
    for i in range(int(n)):
        BordedImage = createborder(OldImage , Iter)
        NewImage = np.array(['?']*len(BordedImage)*len(BordedImage[0])).reshape(len(BordedImage[0]),len(BordedImage))
        BordedImage = createborder(BordedImage , Iter)
        for y in range(len(NewImage)):
            for x in range(len(NewImage[y])):
                IndexForOld = (y+1,x+1)
                Binar = ''
                tes = ''
                for mov in neighbors:
                    char = BordedImage[IndexForOld[0] + mov[0]][IndexForOld[1]+mov[1]]
                    if char == '.':
                        Binar = Binar +"0"
                    else:
                        Binar = Binar + '1'
                    tes =tes + char
                IndexForAlgo = int(Binar,2)
                NewImage[y][x] = Algo[IndexForAlgo]
        OldImage = NewImage
        Iter += 1
    print('Result: %s'%(len(OldImage[OldImage == '#'])))

script(sys.argv[1],sys.argv[2])
