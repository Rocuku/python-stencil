import unittest

from Table import Table
from Cell import Cell

class TestTable(unittest.TestCase):

	def test_gen_random_input(self):
		# given
		table = Table()

		# when
		result = table.get_random_input(3, 2)

		# then
		self.assertEqual(table.height, 3)
		self.assertEqual(table.weight, 2)
		self.assertEqual(3 * 2, len(result))		

	def test_generate_table(self):
		# given
		table = Table()
		height = 3
		weight = 2
		test_matrix = [True, False, False, False, False, False]
		# when
		table.generate_table(height, weight, test_matrix)

		# then
		self.assertTrue(table.cells[0][0].state)
		self.assertFalse(table.cells[0][1].state)
		self.assertFalse(table.cells[1][0].state)
		self.assertFalse(table.cells[1][1].state)
		self.assertFalse(table.cells[2][0].state)
		self.assertFalse(table.cells[2][1].state)

	def test_check_cell_out_table(self):
		table = Table()

		table.height = 3
		table.weight = 2

		is_in_table = table.check_cell_is_in_table(3, 1)

		self.assertFalse(is_in_table)


	def test_check_cell_in_table(self):
		table = Table()

		table.height = 3
		table.weight = 2

		is_in_table = table.check_cell_is_in_table(1, 1)

		self.assertTrue(is_in_table)

	def test_get_number_of_alive_neighbour(self):
		table = Table()

		table.height = 3
		table.weight = 2
		table.cells = [[Cell(True), Cell(False)], [Cell(False), Cell(False)], [Cell(False), Cell(False)]]

		result = table.get_number_of_alive_neighbour(1, 1)

		self.assertEqual(1, result)




		