import unittest

from Cell import Cell

class TestCell(unittest.TestCase):

	def test_should_dead_when_alive_cell_have_less_than2_live_neigbhour(self):
		# given
		cell = Cell(True)
		number_of_alive_neigbhour = 1

		# when
		cell.turn(number_of_alive_neigbhour)

		# then
		self.assertFalse(cell.state)

	def test_should_dead_when_alive_cell_have_more_than3_live_neigbhour(self):
		# given
		cell = Cell(True)
		number_of_alive_neigbhour = 4

		# when
		cell.turn(number_of_alive_neigbhour)

		# then
		self.assertFalse(cell.state)

	def test_alive_should_alive_when_alive_cell_have_equal3_live_neigbhour(self):
		# given
		cell = Cell(True)
		number_of_alive_neigbhour = 3

		# when
		cell.turn(number_of_alive_neigbhour)

		# then
		self.assertTrue(cell.state)

	def test_dead_should_alive_when_alive_cell_have_equal3_live_neigbhour(self):
		# given
		cell = Cell(False)
		number_of_alive_neigbhour = 3

		# when
		cell.turn(number_of_alive_neigbhour)

		# then
		self.assertTrue(cell.state)

	def test_dead_should_dead_when_alive_cell_have_equal2_live_neigbhour(self):
		# given
		cell = Cell(False)
		number_of_alive_neigbhour = 2

		# when
		cell.turn(number_of_alive_neigbhour)

		# then
		self.assertFalse(cell.state)

	def test_alive_should_alive_when_alive_cell_have_equal2_live_neigbhour(self):
		# given
		cell = Cell(True)
		number_of_alive_neigbhour = 2

		# when
		cell.turn(number_of_alive_neigbhour)

		# then
		self.assertTrue(cell.state)