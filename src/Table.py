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

	def check_cell_is_in_table(self, h, w):
		if h < self.height and w < self.weight and h >= 0 and w >= 0:
			return True
		else: 
			return False

	def get_number_of_alive_neighbour(self, h, w):
		number_of_alive_neighbour = 0
		if self.check_cell_is_in_table(h, w):
			if self.check_cell_is_in_table(h + 1, w + 1):
				if self.cells[h + 1][w + 1].state:
					number_of_alive_neighbour += 1
			if self.check_cell_is_in_table(h + 1, w):
				if self.cells[h + 1][w].state:
					number_of_alive_neighbour += 1
			if self.check_cell_is_in_table(h + 1, w - 1):
				if self.cells[h + 1][w - 1].state:
					number_of_alive_neighbour += 1
			if self.check_cell_is_in_table(h, w + 1):
				if self.cells[h][w + 1].state:
					number_of_alive_neighbour += 1
			if self.check_cell_is_in_table(h, w - 1):
				if self.cells[h][w - 1].state:
					number_of_alive_neighbour += 1
			if self.check_cell_is_in_table(h - 1, w + 1):
				if self.cells[h - 1][w + 1].state:
					number_of_alive_neighbour += 1
			if self.check_cell_is_in_table(h - 1, w):
				if self.cells[h - 1][w].state:
					number_of_alive_neighbour += 1
			if self.check_cell_is_in_table(h - 1, w - 1):
				if self.cells[h - 1][w - 1].state:
					number_of_alive_neighbour += 1

		return number_of_alive_neighbour





		

