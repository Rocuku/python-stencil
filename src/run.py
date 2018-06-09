# coding: utf-8
from Table import Table
from Cell import Cell
import time, os

if __name__ == '__main__':
	table = Table("./test_case/test_case_1")
	while 1:
		table.next_generation()
		os.system('clear')
		print(table.show_table())
		time.sleep(1)

