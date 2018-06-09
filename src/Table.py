class Table(object):
	def __init__(self):
		self.cell = []
		self.shape = [9, 9]

	def input(self, input_string):
		temp = input_string.split()[0]
		self.shape[0] = int(temp.split(',')[0])
		self.shape[1] = int(temp.split(',')[1])



