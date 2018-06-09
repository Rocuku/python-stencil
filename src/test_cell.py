import unittest

from Cell import Cell

class TestCell(unittest.TestCase):

	def test_should_dead_when_alive_cell_have_less_than2_live_neighbour(self):
		# given
		cell = Cell(True)
		number_of_alive_neighbour = 1

		# when
		cell.turn(number_of_alive_neighbour)

		# then
		self.assertFalse(cell.state)

	def test_should_dead_when_alive_cell_have_more_than3_live_neighbour(self):
		# given
		cell = Cell(True)
		number_of_alive_neighbour = 4

		# when
		cell.turn(number_of_alive_neighbour)

		# then
		self.assertFalse(cell.state)

	def test_alive_should_alive_when_alive_cell_have_equal3_live_neighbour(self):
		# given
		cell = Cell(True)
		number_of_alive_neighbour = 3

		# when
		cell.turn(number_of_alive_neighbour)

		# then
		self.assertTrue(cell.state)

	def test_dead_should_alive_when_alive_cell_have_equal3_live_neighbour(self):
		# given
		cell = Cell(False)
		number_of_alive_neighbour = 3

		# when
		cell.turn(number_of_alive_neighbour)

		# then
		self.assertTrue(cell.state)

	def test_dead_should_dead_when_alive_cell_have_equal2_live_neighbour(self):
		# given
		cell = Cell(False)
		number_of_alive_neighbour = 2

		# when
		cell.turn(number_of_alive_neighbour)

		# then
		self.assertFalse(cell.state)

	def test_alive_should_alive_when_alive_cell_have_equal2_live_neighbour(self):
		# given
		cell = Cell(True)
		number_of_alive_neighbour = 2

		# when
		cell.turn(number_of_alive_neighbour)

		# then
		self.assertTrue(cell.state)