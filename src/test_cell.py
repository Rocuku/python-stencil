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