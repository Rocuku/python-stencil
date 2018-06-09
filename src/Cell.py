class Cell(object):
	def __init__(self, state):
		self.state = state

	def turn(self, number_of_alive_neighbour):
		if number_of_alive_neighbour < 2:
			self.state = False

		if number_of_alive_neighbour > 3:
			self.state = False

		if number_of_alive_neighbour == 3:
			self.state = True

		if number_of_alive_neighbour == 2:
			self.state = self.state

	def get_number_of_alive_neighbour():
		pass