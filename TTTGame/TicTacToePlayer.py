from TTTGame.Coordinate import *
from TTTGame.TicTacToeGrid import *
from IA.model import *
from IA.layers import *
from IA.losses import *
from IA.optimizers import *
import random

class TicTacToePlayer :
    name : str
    def __init__(self, name=""):
        self.name = name
    def play(self, gridTTT : TicTacToesGrid)->Coordinate:
        pass
    def name(self):
        return self.name

class RandomTrainer(TicTacToePlayer):
    def __init__(self):
        super().__init__("RandomTrainer")
    def play(self, gridTTT : TicTacToesGrid)->Coordinate:
        choices = getPossibleMooves(gridTTT)
        return choices[random.randint(0, len(choices)-1)]

class DeepLearningPlayer(TicTacToePlayer):
    model : Model
    def __init__(self, name : str):
        super().__init__(name)
        self.model = Model()

    def play(self, gridTTT : TicTacToesGrid)->Coordinate:
        pass

class Najarala(DeepLearningPlayer):

    def __init__(self):
        super().__init__("Najarala bot")
        self.model.add(Input(18))
        self.model.add(Linear(15))
        self.model.add(Tanh())
        self.model.add(Linear(12))
        self.model.add(Tanh())
        self.model.add(Linear(9))
        self.model.add(Softmax())
        self.model.compile(MeanSquaredError(), SGD())

    def play(self, gridTTT : TicTacToesGrid)->Coordinate:
        self.model.forward(getBinaryInput(gridTTT))

class HumanPlayer(TicTacToePlayer):
    def __init__(self, name : str):
        super().__init__(name)
    def play(self, gridTTT : TicTacToesGrid)->Coordinate:
        choices = getPossibleMooves(gridTTT)
        while True :
            choice = str(input(super().name() + " choisissez votre case en suivant le schéma ci dessus : "))
            if(choice.isdigit() and int(choice) >= 1 and int(choice) <= 9):
                x = (int(choice) - 1) % 3
                y = 2 - (int(choice) - 1) // 3
                if(isCoordinateInList(x, y, choices)) : return Coordinate(x, y)
