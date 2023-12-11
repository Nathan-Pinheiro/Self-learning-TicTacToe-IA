import os
import random
from TTTGame import TicTacToePlayer as TTTPlayer
from TTTGame import Coordinate as C
from TTTGame import TicTacToeGrid as TTTGrid

def changeTurn(isTurnP1 : bool)->bool:
    return not isTurnP1

def __couleur(symbole : str)->str:
    B  = '\033[94m' # blue
    R  = '\033[91m' # red
    W  = '\033[0m'  # white (normal)
    if(symbole == 'X'): return B
    elif(symbole == 'O'): return R
    else: return W

def __afficherMenu(gridTTT : TTTGrid.TicTacToesGrid):

    W  = '\033[0m'  # white (normal)

    os.system("cls")
    print("---------------------------------------------")
    print("Schéma :")
    print("7 | 8 | 9")
    print("4 | 5 | 6")
    print("1 | 2 | 3")
    print("---------------------------------------------")
    print("Partie :")
    print(TTTGrid.getBinaryInput(gridTTT))
    print(__couleur(gridTTT.getGrid()[0][0]) + gridTTT.getGrid()[0][0] + W + " | " + __couleur(gridTTT.getGrid()[1][0]) + gridTTT.getGrid()[1][0] + W + " | " + __couleur(gridTTT.getGrid()[2][0]) + gridTTT.getGrid()[2][0] + W)
    print(__couleur(gridTTT.getGrid()[0][1]) + gridTTT.getGrid()[0][1] + W + " | " + __couleur(gridTTT.getGrid()[1][1]) + gridTTT.getGrid()[1][1] + W + " | " + __couleur(gridTTT.getGrid()[2][1]) + gridTTT.getGrid()[2][1] + W)
    print(__couleur(gridTTT.getGrid()[0][2]) + gridTTT.getGrid()[0][2] + W + " | " + __couleur(gridTTT.getGrid()[1][2]) + gridTTT.getGrid()[1][2] + W + " | " + __couleur(gridTTT.getGrid()[2][2]) + gridTTT.getGrid()[2][2] + W)
    print("---------------------------------------------")
    os.system("pause")

def __affichageFin(gridTTT : TTTGrid.TicTacToesGrid, victory : int ):

    W  = '\033[0m'  # white (normal)

    os.system("cls")
    print("---------------------------------------------")
    print("Partie Terminée :")
    if(victory == 0): print("Egalité !")
    elif(victory == 1): print("Victoire du joueur 1 !")
    else: print("Victoire du joueur 2 !")
    print("---------------------------------------------")
    print("Partie :")
    print(__couleur(gridTTT.getGrid()[0][0]) + gridTTT.getGrid()[0][0] + W + " | " + __couleur(gridTTT.getGrid()[1][0]) + gridTTT.getGrid()[1][0] + W + " | " + __couleur(gridTTT.getGrid()[2][0]) + gridTTT.getGrid()[2][0] + W)
    print(__couleur(gridTTT.getGrid()[0][1]) + gridTTT.getGrid()[0][1] + W + " | " + __couleur(gridTTT.getGrid()[1][1]) + gridTTT.getGrid()[1][1] + W + " | " + __couleur(gridTTT.getGrid()[2][1]) + gridTTT.getGrid()[2][1] + W)
    print(__couleur(gridTTT.getGrid()[0][2]) + gridTTT.getGrid()[0][2] + W + " | " + __couleur(gridTTT.getGrid()[1][2]) + gridTTT.getGrid()[1][2] + W + " | " + __couleur(gridTTT.getGrid()[2][2]) + gridTTT.getGrid()[2][2] + W)
    print("---------------------------------------------")
    os.system("pause")

def LaunchGame(p1 : TTTPlayer.TicTacToePlayer, p2 : TTTPlayer.TicTacToePlayer, displays : bool) -> int:

    gridTTT = TTTGrid.TicTacToesGrid('X', 'O', '.')

    isTurnP1 : bool
    isTurnP1 = bool(random.getrandbits(1))

    moove : C.Coordinate
    winState = (False, 0)

    while not winState[0]:

        if(displays): __afficherMenu(gridTTT)

        if(isTurnP1): moove = p1.play(gridTTT)
        else: moove = p2.play(gridTTT)

        gridTTT.play(moove, isTurnP1)

        winState = TTTGrid.checkWin(gridTTT)
        isTurnP1 = __changeTurn(isTurnP1)

    if(displays): __affichageFin(gridTTT, winState[1])
    return winState[1]

def trainAIByAmount(p1 : TTTPlayer.TicTacToePlayer, p2 : TTTPlayer.TicTacToePlayer, iterations : int, gamePerIterations : int):

    equalities : int
    p1victories : int
    p1victories : int

    os.system("cls")
    print("----------------------------------------------")

    for i in range(iterations):

        equalities = 0
        p1victories = 0
        p2victories = 0

        for j in range(gamePerIterations):

            result = LaunchGame(p1, p2, False)
            if(result == 0): equalities += 1
            elif(result == 1): p1victories += 1
            else: p2victories += 1

        print("Itération : " + str(i + 1))
        print("Egalités : " + str(equalities) + " | Victoire P1 : " + str(p1victories) + " | Victoire P2 : " + str(p2victories))
        print("----------------------------------------------")

    os.system("pause")

def trainAI(p1 : TTTPlayer.TicTacToePlayer, p2 : TTTPlayer.TicTacToePlayer):
    trainAIByAmount(p1, p2, 5, 5000)