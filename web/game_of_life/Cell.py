class Cell(object):
	def __init__(self, state):
		self.state = state
		self.next_state = state

	def get_next_state(self, number_of_alive_neighbour):
		if number_of_alive_neighbour < 2:
			self.next_state = False

		if number_of_alive_neighbour > 3:
			self.next_state = False

		if number_of_alive_neighbour == 3:
			self.next_state = True

		if number_of_alive_neighbour == 2:
			self.next_state = self.state

	def turn(self):
		self.state = self.next_state
