from TTTGame import Coordinate as C

class TicTacToesGrid :
    p1chr : chr
    p2chr : chr
    voidChr : chr
    grid : list[list[chr]]

    def __init__(self, p1chr : chr, p2chr : chr, voidChr : chr):
        self.p1chr = p1chr
        self.p2chr = p2chr
        self.voidChr = voidChr
        self.grid = [[voidChr,voidChr,voidChr],[voidChr,voidChr,voidChr],[voidChr,voidChr,voidChr]]

    def __str__(self):
        return self.grid[0][0] + " | " + self.grid[0][1] + " | " + self.grid[0][2] + "\n" + self.grid[1][0] + " | " + self.grid[1][1] + " | " + self.grid[1][2] + "\n" + self.grid[2][0] + " | " + self.grid[2][1] + " | " + self.grid[2][2]

    def getGrid(self)->list[list[chr]]: return self.grid

    def play(self, moove : C.Coordinate, isTurnP1 : bool)->bool:
        if(moove.x < 3 and moove.x >= 0 and moove.y < 3 and moove.y >= 0 and self.getGrid()[moove.x][moove.y] == self.voidChr):
            if(isTurnP1): self.getGrid()[moove.x][moove.y] = self.p1chr
            else: self.getGrid()[moove.x][moove.y] = self.p2chr
            return True
        else: return False

def checkEquality(gridTTT : TicTacToesGrid)->bool:
    equality : bool
    equality = True
    for i in range(0, len(gridTTT.getGrid())) :
        for j in range(0, len(gridTTT.getGrid()[i])) :
            if(gridTTT.getGrid()[i][j] == '.'): equality = False
    return equality

def checkWin(gridTTT : TicTacToesGrid):
    #checking for vertical lines
    for i in range(len(gridTTT.getGrid())):
        lastCar = ''
        for j in range(len(gridTTT.getGrid()[i])):
            if(lastCar != gridTTT.getGrid()[i][j] and lastCar != ''): break
            elif(len(gridTTT.getGrid()[i]) - 1 == j):
                if(lastCar == gridTTT.p1chr): return (True, 1)
                elif(lastCar == gridTTT.p2chr): return (True, 2)
            else: lastCar = gridTTT.getGrid()[i][j]
    #checking for horizontal lines
    for i in range(len(gridTTT.getGrid())):
        lastCar = ''
        for j in range(len(gridTTT.getGrid()[i])):
            if(lastCar != gridTTT.getGrid()[j][i] and lastCar != ''): break
            elif(len(gridTTT.getGrid()[i]) - 1 == j):
                if(lastCar == gridTTT.p1chr): return (True, 1)
                elif(lastCar == gridTTT.p2chr): return (True, 2)
            else: lastCar = gridTTT.getGrid()[j][i]
    #checking for desc diagonals
    lastCar = ''
    for i in range(len(gridTTT.getGrid())):
        if(lastCar != gridTTT.getGrid()[i][i] and lastCar != ''): break
        elif(len(gridTTT.grid[i]) - 1 == i):
            if(lastCar == gridTTT.p1chr): return (True, 1)
            elif(lastCar == gridTTT.p2chr): return (True, 2)
        else: lastCar = gridTTT.getGrid()[i][i]
    #checking for asc diagonals
    lastCar = ''
    for i in range(len(gridTTT.getGrid())):
        if(lastCar != gridTTT.getGrid()[i][len(gridTTT.getGrid()) - 1 - i] and lastCar != ''): break
        elif(len(gridTTT.getGrid()[i]) - 1 == i):
            if(lastCar == gridTTT.p1chr): return (True, 1)
            elif(lastCar == gridTTT.p2chr): return (True, 2)
        else: lastCar = gridTTT.getGrid()[i][len(gridTTT.getGrid()) - 1 - i]
    #checking for equality
    if(checkEquality(gridTTT)): return (True, 0)
    return (False, 0)

def getPossibleMooves(gridTTT : TicTacToesGrid)->list[C.Coordinate]:
    mooves : list[C.Coordinate]
    mooves = []
    for i in range(0, len(gridTTT.getGrid())):
        for j in range(0, len(gridTTT.getGrid()[i])):
            if(gridTTT.getGrid()[i][j] == '.'): mooves.append(C.Coordinate(i,j))
    return mooves

def getPossibleMoovesToInt(gridTTT : TicTacToesGrid)->list[int]:
    mooves : list[C.Coordinate]
    mooves = []
    for i in range(0, len(gridTTT.getGrid())):
        for j in range(0, len(gridTTT.getGrid()[i])):
            if(gridTTT.getGrid()[i][j] == '.'): mooves.append(i * 3 + j)
    return mooves

def getBinaryInput(gridTTT : TicTacToesGrid)->list[int]:

    binaryInputs : list[int]
    binaryInputs = []
    for i in range(0, len(gridTTT.getGrid())):
        for j in range(0, len(gridTTT.getGrid()[i])):
            if(gridTTT.getGrid()[j][i] == gridTTT.p1chr): binaryInputs.append(1)
            else: binaryInputs.append(0)

    for i in range(0, len(gridTTT.getGrid())):
        for j in range(0, len(gridTTT.getGrid()[i])):
            if(gridTTT.getGrid()[j][i] == gridTTT.p2chr): binaryInputs.append(1)
            else: binaryInputs.append(0)

    return binaryInputs