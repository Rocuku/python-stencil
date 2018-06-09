import random
from Cell import Cell

class Table(object):
	def __init__(self):
		self.cells = []
		self.height = 9
		self.weight = 9

	def get_random_input(self, height, weight):
		self.height = height
		self.weight = weight
		temp = []
		for x in range(height * weight):
			temp.append(bool(random.getrandbits(1)))
		return temp

	def generate_table(self, height, weight, test_matrix):
		for i in range(height):
			temp = []
			for j in range(weight):
				temp.append(Cell(test_matrix[i * weight + j]))
			self.cells.append(temp)


