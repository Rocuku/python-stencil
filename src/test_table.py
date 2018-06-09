import unittest

from Table import Table

class TestTable(unittest.TestCase):

	def test_input_should_get_and_save_shape(self):
		# given
		table = Table()

		# when
		table.input("3,2 110100")

		# then
		self.assertEqual(table.shape[0], 3)
		self.assertEqual(table.shape[1], 2)