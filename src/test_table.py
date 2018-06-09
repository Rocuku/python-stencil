import unittest

from Table import Table

class TestTable(unittest.TestCase):

	def test_gen_random_input(self):
		# given
		table = Table()

		# when
		table.get_random_input(3, 2)

		# then
		self.assertEqual(table.height, 3)
		self.assertEqual(table.weight, 2)		



		