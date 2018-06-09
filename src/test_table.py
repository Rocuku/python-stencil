import unittest

from Table import Table
from Cell import Cell

class TestTable(unittest.TestCase):

	def test_gen_random_input(self):
		# given
		table = Table(height = 3, weight = 2)

		# when
		result = table.get_random_input()

		# then
		self.assertEqual(table.height, 3)
		self.assertEqual(table.weight, 2)
		self.assertEqual(3 * 2, len(result))		

	def test_generate_table(self):
		# given
		table = Table(height = 3, weight = 2)
		flatten_table = [True, False, False, False, False, False]
		# when
		table.generate_table(flatten_table)

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

	def test_next_generation(self):
		table = Table()

		table.height = 3
		table.weight = 3
		table.cells = [[Cell(False), Cell(False), Cell(False)], 
						[Cell(True), Cell(True), Cell(True)], 
						[Cell(False), Cell(False), Cell(False)]]

		table.next_generation()

		self.assertFalse(table.cells[0][0].state)
		self.assertTrue(table.cells[0][1].state)
		self.assertFalse(table.cells[0][2].state)

		self.assertFalse(table.cells[1][0].state)
		self.assertTrue(table.cells[1][1].state)
		self.assertFalse(table.cells[1][2].state)

		self.assertFalse(table.cells[2][0].state)
		self.assertTrue(table.cells[2][1].state)
		self.assertFalse(table.cells[2][2].state)

	def test_get_input_table_from_file(self):
		table = Table()

		file_path = "./test_case/test_case_1"
		flatten_table = table.get_file_input(file_path)

		self.assertEqual(table.height,3)
		self.assertEqual(table.weight,3)
		self.assertFalse(flatten_table[0])
		self.assertFalse(flatten_table[1])
		self.assertFalse(flatten_table[2])
		self.assertTrue(flatten_table[3])
		self.assertTrue(flatten_table[4])
		self.assertTrue(flatten_table[5])
		self.assertFalse(flatten_table[6])
		self.assertFalse(flatten_table[7])
		self.assertFalse(flatten_table[8])


	def test_show_table(self):
		table = Table()

		table.height = 3
		table.weight = 3
		table.cells = [[Cell(False), Cell(False), Cell(False)], 
						[Cell(True), Cell(True), Cell(True)], 
						[Cell(False), Cell(False), Cell(False)]]

		show=table.show_table()
		self.assertEqual(show, "XXX\nOOO\nXXX")




		