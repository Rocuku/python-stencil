import unittest

from Table import Table

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





		