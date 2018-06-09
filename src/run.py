# coding: utf-8
from Table import Table
from Cell import Cell
import time, os

if __name__ == '__main__':
	table = Table()
	height, weight, value = table.get_file_input("./test_case/test_case_1")
	table.generate_table(height, weight, value)
	while 1:
		table.next_generation()
		os.system('clear')
		print(table.show_table())
		time.sleep(1)

