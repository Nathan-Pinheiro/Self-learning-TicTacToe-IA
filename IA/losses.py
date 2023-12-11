import numpy as np

class Loss:

	def __init__(self):
		pass

	def forward(self, output, target):
		pass

	def backward(self, output, target):
		pass

class MeanSquaredError(Loss):

	def forward(self, output, target):
		return np.mean((output - target) ** 2)

	def backward(self, output, target):
		return output - target