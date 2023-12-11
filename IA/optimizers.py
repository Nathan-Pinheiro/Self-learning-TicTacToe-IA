import numpy as np
from .layers import Parameter

class Optimizer:

	def init(self):
		pass

	def update(self, layers):
		pass

	def iteration(self):
		pass


class SGD(Optimizer):

	def __init__(self, learning_rate = 0.01, momentum = 0.9):
		self.learning_rate = learning_rate
		self.momentum = momentum

	def init(self):
		pass

	def update(self, layers):
		for layer in layers:
			if isinstance(layer, Parameter):
				for i in range(len(layer.weights)):
					layer.velocities[i] = (self.momentum * layer.velocities[i]) + ((1. - self.momentum) * layer.gradients[i])
					layer.weights[i] -= layer.velocities[i] * self.learning_rate

	def iteration(self):
		pass
