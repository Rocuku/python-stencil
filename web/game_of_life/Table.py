import random
from Cell import Cell

class Table(object):
	def __init__(self, file_path = None, height = 9, weight = 9):
		self.cells = []
		self.height = height
		self.weight = weight
		if file_path:
			flatten_table = self.get_file_input(file_path)
		else:
			flatten_table = self.get_random_input()
		self.generate_table(flatten_table)

	def get_random_input(self):
		flatten_table = []
		for x in range(self.height * self.weight):
			flatten_table.append(bool(random.getrandbits(1)))
		return flatten_table

	def get_file_input(self, file_path):
		self.height = 0
		self.weight = 0
		flatten_table = []
		with open(file_path) as file:
			for line in file:
				self.height += 1
				self.weight = 0
				value_list = line.split()
				for val in value_list:
					self.weight += 1
					flatten_table.append(int(val) == 1)
		return flatten_table

	def generate_table(self, flatten_table):
		self.cells = []
		for h in range(self.height):
			temp = []
			for w in range(self.weight):
				temp.append(Cell(flatten_table[h * self.weight + w]))
			self.cells.append(temp)

	def check_cell_is_in_table(self, h, w):
		return h < self.height and w < self.weight and h >= 0 and w >= 0

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

	def get_next_state(self):
		for h in range(self.height):
			for w in range(self.weight):
				number_of_alive_neighbour = self.get_number_of_alive_neighbour(h, w)
				self.cells[h][w].get_next_state(number_of_alive_neighbour)

	def set_state(self):
		for h in range(self.height):
			for w in range(self.weight):
				self.cells[h][w].turn()

	def next_generation(self):
		self.get_next_state()
		self.set_state()



	def show_table(self):
		show = ""
		for i in range(self.height):
			for j in range(self.weight):
				show = show + '*' if self.cells[i][j].state else show + 'o'
			show += '<br />'
		return show[: len(show) - 2]


		

