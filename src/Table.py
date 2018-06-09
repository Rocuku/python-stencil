import random

class Table(object):
	def __init__(self):
		self.cell = []
		self.height = 9
		self.weight = 9

	def input(self, input_string):
		temp = input_string.split()[0]
		self.shape[0] = int(temp.split(',')[0])
		self.shape[1] = int(temp.split(',')[1])

	def get_random_input(self, height, weight):
		self.height = height
		self.weight = weight
		temp = []
		for x in range(height * weight):
			temp.append(bool(random.getrandbits(1)))
		return temp



