def script():
    data = [[[51,651,86],[948,9849,615],[98,98,784]],[[1,2,3],[4,5,6],[7,8,9]]]
    BeaconMap = [[1,5,6],[1,9,7],[87,9,6]]
    BeaconMap_Copy = BeaconMap[:]
    TotalBeaconsNumber = 50
    ScannerMap = [[0,0,0]]
    CheckedScanner = [0]
    while len(BeaconMap) != TotalBeaconsNumber:
        AbsDistMap = [[8,9,948,94984,4,9484],[894,9486,648,616],[89,65,849,948]]
        for NumScannerToLook in range(len(data)):
            print('FOO1')
            if NumScannerToLook in CheckedScanner:
                continue
            ScannerToLookDistMap = [[1,2,3,4,5,6],[7,8,9,10],[11,12,13,14]]
            for NumBeaconAbs in range(len(AbsDistMap)):
                for NumBeaconToLook in range(len(ScannerToLookDistMap)):
                    print(NumBeaconAbs,NumBeaconToLook)
script()
