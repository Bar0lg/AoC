import sys,os,time,math
import numpy as np


mov = {((0, 0, 1), (-1, 0, 0), (0, -1, 0)), ((-1, 0, 0), (0, 0, 1), (0, 1, 0)), ((0, 1, 0), (1, 0, 0), (0, 0, -1)), ((0, 1, 0), (0, 0, 1), (1, 0, 0)), ((-1, 0, 0), (0, 0, -1), (0, -1, 0)), ((1, 0, 0), (0, 0, 1), (0, -1, 0)), ((0, 0, 1), (0, 1, 0), (-1, 0, 0)), ((0, 0, -1), (1, 0, 0), (0, -1, 0)), ((0, 1, 0), (0, 0, -1), (-1, 0, 0)), ((1, 0, 0), (0, 0, -1), (0, 1, 0)), ((0, -1, 0), (0, 0, 1), (-1, 0, 0)), ((0, 0, -1), (-1, 0, 0), (0, 1, 0)), ((-1, 0, 0), (0, 1, 0), (0, 0, -1)), ((0, 0, 1), (0, -1, 0), (1, 0, 0)), ((0, -1, 0), (-1, 0, 0), (0, 0, -1)), ((0, -1, 0), (0, 0, -1), (1, 0, 0)), ((0, 1, 0), (-1, 0, 0), (0, 0, 1)), ((1, 0, 0), (0, -1, 0), (0, 0, -1)), ((0, 0, -1), (0, -1, 0), (-1, 0, 0)), ((0, -1, 0), (1, 0, 0), (0, 0, 1)), ((0, 0, -1), (0, 1, 0), (1, 0, 0)), ((-1, 0, 0), (0, -1, 0), (0, 0, 1)), ((1, 0, 0), (0, 1, 0), (0, 0, 1)), ((0, 0, 1), (1, 0, 0), (0, 1, 0))}


def recupfile(file):
    f = open(file,'r').read().split('\n\n')
    f = [i.split('\n') for i in f]
    [i.pop(0) for i in f]
    data = [[i.split(',') for i in k]for k in f]
    data[-1].pop(-1)
    return data

def deletedouble(liste):
    res = []
    for i in liste:
        if i not in res:
            res.append(i)
    return res

def convert_rec(x):
    if isinstance(x, list):
        return list(map(convert_rec, x))
    else:
        return int(x)

def occurance(list1,list2):
    res = 0
    for i in list1:
        if i in list2:
            res += 1
    return res

def mulvectors(coo,mov):
    x = coo[0] * mov[0][0] + coo[1] * mov[0][1] + coo[2] * mov[0][2]
    y = coo[0] * mov[1][0] + coo[1] * mov[1][1] + coo[2] * mov[1][2]
    z = coo[0] * mov[2][0] + coo[1] * mov[2][1] + coo[2] * mov[2][2]
    return [x,y,z]

def createDistMap(Coordinates):
    res = [[] for i in range(len(Coordinates))]
    for i in range(len(Coordinates)):
        for k in Coordinates:
            res[i].append(math.floor(math.sqrt((Coordinates[i][0] - k[0])**2 + (Coordinates[i][1] - k[1])**2 + (Coordinates[i][2] - k[2])**2 )))
    return res


def findManathan(liste):
    res = 0
    invliste = [[k[i]*-1 for i in range(3)]for k in liste]
    for i in liste:
        for k in invliste:
            if sum([i[j] + k[j] for j in range(3)]) > res:
                res = sum([i[j] + k[j] for j in range(3)])
    return res

def script(file):
    data = convert_rec(recupfile(file))
    print("Creating map...")
    BeaconMap = data[0]
    BeaconMap_Copy = BeaconMap[:]
    ScannerMap = [[0,0,0]]
    CheckedScanner = [0]
    for passes in range(len(data)):
        print(len(BeaconMap))
        AbsDistMap = createDistMap(BeaconMap)
        for NumScannerToLook in range(len(data)):
            if NumScannerToLook in CheckedScanner:
                continue
            ScannerToLookDistMap = createDistMap(data[NumScannerToLook])
            for NumBeaconAbs in range(len(AbsDistMap)):
                for NumBeaconToLook in range(len(ScannerToLookDistMap)):
                    if occurance(AbsDistMap[NumBeaconAbs],ScannerToLookDistMap[NumBeaconToLook]) > 11:
                        print("Find Matching Beacon")
                        CooBeaconAbs = BeaconMap_Copy[NumBeaconAbs]
                        CooBeaconToLook = data[NumScannerToLook][NumBeaconToLook]
                        MapFromBeaconAbs = [[k[i] - CooBeaconAbs[i] for i in range(3)] for k in BeaconMap_Copy]
                        MapFromBeaconToLook = [[k[i] - CooBeaconToLook[i] for i in range(3)] for k in data[NumScannerToLook]]
                        print("Rotating Plane....")
                        for MovmentToApply in mov:
                            NewCoo = [mulvectors(i,MovmentToApply) for i in MapFromBeaconToLook]
                            if occurance(MapFromBeaconAbs,NewCoo) > 11:
                                print("Found movment")
                                MapBeaconToLookShifted = [mulvectors(i,MovmentToApply) for i in data[NumScannerToLook]]
                                CooScannerToLookAbs = [CooBeaconAbs[i] + MapBeaconToLookShifted[NumBeaconToLook][i]*-1 for i in range(3)]
                                ScannerMap.append(CooScannerToLookAbs)
                                CheckedScanner.append(NumScannerToLook)
                                MapBeaconToLookAbs = [[k[i] + CooScannerToLookAbs[i] for i in range(3)] for k in MapBeaconToLookShifted]
                                print('Inserting New Beacon...')
                                for i in MapBeaconToLookAbs:
                                    if i not in BeaconMap_Copy:
                                        BeaconMap_Copy.append(i)
        BeaconMap = BeaconMap_Copy[:]
    print(findManathan(deletedouble(ScannerMap)))
file = str(sys.argv[1])
script(file)
