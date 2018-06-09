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
		offset = [[-1, -1], [-1, 0], [-1, 1],
				[0, -1],  [0, 1],
				[1, -1], [1, 0], [1, 1]]
		for i in range(8):
				if self.check_cell_is_in_table(h + offset[i][0], w + offset[i][1]) and \
							self.cells[h + offset[i][0]][w + offset[i][1]].state:
					number_of_alive_neighbour += 1	

		return number_of_alive_neighbour

	def next_generation(self):
		for i in range(self.height):
			for j in range(self.weight):
				number_of_alive_neighbour = self.get_number_of_alive_neighbour(i, j)
				self.cells[i][j].get_next_state(number_of_alive_neighbour)

		for i in range(self.height):
			for j in range(self.weight):
				self.cells[i][j].turn()




		

