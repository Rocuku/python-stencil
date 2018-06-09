class Cell(object):
	def __init__(self, state):
		self.state = state

	def turn(self, number_of_alive_neigbhour):
		if number_of_alive_neigbhour < 2:
			self.state = False