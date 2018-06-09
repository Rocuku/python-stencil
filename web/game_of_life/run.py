# coding: utf-8
from Table import Table
from Cell import Cell
import time, os
import sys

if __name__ == '__main__':

	table = Table(weight = 100, height = 100)
	while 1:
		os.system('clear')
		print(table.show_table())
		table.next_generation()
		time.sleep(1)

