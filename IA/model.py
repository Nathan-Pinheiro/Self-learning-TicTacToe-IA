from copy import deepcopy
from .layers import *
from .optimizers import *
from .losses import *
from . import utils
from TTTGame import TicTacToe as TTT
from TTTGame import TicTacToePlayer as TTTPlayer
from TTTGame import TicTacToeGrid as TTTGrid
from TTTGame.Coordinate import *
import os
import math
import random

class Model:

	def __init__(self):
		self.layers = []

	def add(self, layer):

		if not isinstance(layer, Layer):
			raise TypeError("Layer must be an instance of Layer")

		if len(self.layers) > 0:
			if type(layer) == Input:
				raise Exception("Input layer cannot be added after other layers")
			layer.create(self.layers[-1].output_size)
		elif type(layer) != Input:
			raise Exception("First layer must be an input layer")
		else:
			self.input_size = layer.input_size

		self.layers.append(layer)

	def compile(self, loss, optimizer):

		if not isinstance(optimizer, Optimizer):
			raise TypeError("Optimizer must be an instance of Optimizer")
		if not isinstance(loss, Loss):
			raise TypeError("Loss must be an instance of Loss")

		self.optimizer = optimizer
		self.loss = loss

		for i in range(len(self.layers) - 1):
			if type(self.layers[i]) == Softmax:
				raise Exception("Softmax layer must be the last layer")
			elif isinstance(self.layers[i], Parameter):
				self.layers[i].init(self.layers[i + 1])

		if isinstance(self.layers[-1], Parameter):
			self.layers[-1].init(None)

		self.output_size = self.layers[-1].output_size

	def forward(self, input):

		for layer in self.layers:
			input = layer.forward(input)

		return input

	def backward(self, reward : float):
		for layer in reversed(self.layers):
			layer.backward(reward)
		self.optimizer.update(self.layers)

	def clear_gradients(self):
		for layer in self.layers:
			if isinstance(layer, Parameter):
				for gradient in layer.gradients:
					gradient[:] = 0

	def average_gradients(self, batch_size):
		for layer in self.layers:
			if isinstance(layer, Parameter):
				for gradient in layer.gradients:
					gradient /= batch_size

	def train(self, oponent : TTTPlayer, iterations : int, gamePerIteration : int):

		equalities : int
		p1victories : int
		p2victories : int

		self.optimizer.init()

		os.system("cls")
		print("----------------------------------------------")

		for i in range(iterations):
			equalities = 0
			p1victories = 0
			p2victories = 0

			for j in range(gamePerIteration):

				self.clear_gradients()
				result = self.trainingGame(oponent)

				if(result == 0):
					equalities += 1
					self.backward(-1)

				elif(result == 1):
					p1victories += 1
					self.backward(10)

				else:
					p2victories += 1
					self.backward(-10)

			print("Itération : " + str(i + 1))
			print("Egalités : " + str(equalities) + " | Victoire P1 : " + str(p1victories) + " | Victoire P2 : " + str(p2victories))
			print("----------------------------------------------")

		os.system("pause")

	def trainingGame(self, oponent : TTTPlayer) :
		gridTTT = TTTGrid.TicTacToesGrid('X', 'O', '.')

		isTurnP1 : bool
		isTurnP1 = bool(random.getrandbits(1))

		moove : Coordinate
		winState = (False, 0)

		while not winState[0]:

			if(isTurnP1):
				while(True):
					result = self.forward(TTTGrid.getBinaryInput(gridTTT)).argmax()
					possibleMooves = TTTGrid.getPossibleMoovesToInt(gridTTT)

					isMoovePossible = False
					for m in possibleMooves:
						print(result)
						print(m)
						if(m == result): isMoovePossible = True

					if(isMoovePossible): self.backward(-10)
					else: break

			else: moove = oponent.play(gridTTT)

			gridTTT.play(moove, isTurnP1)

			winState = TTTGrid.checkWin(gridTTT)
			isTurnP1 = TTT.changeTurn(isTurnP1)

		return winState[1]

	def predict(self, x):
		output = self.forward(x)
		return output.argmax()

	def test(self, x, y, check_data = True, print_results = True):

		if check_data:
			x_copy, y_copy = self.check_input(x, y)
		else:
			x_copy, y_copy = x, y

		nb_data = x.shape[0]
		loss = 0
		accuracy = 0

		for i in range(nb_data):

			output = self.forward(x_copy[i])
			loss += self.loss.forward(output, y_copy[i])

			if output.argmax() == y_copy[i]:
				accuracy += 1

		if print_results:
			print("Test loss: %.2f | test accuracy: %.1f%%" % (loss / nb_data, (accuracy / nb_data) * 100.))

		return accuracy / nb_data, loss / nb_data
