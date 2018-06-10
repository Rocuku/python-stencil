# coding: utf-8
from Table import Table
from Cell import Cell
import time, os
import sys

if __name__ == '__main__':
	file_path = None
	weight = 9
	height = 9
	time_slot = 1

	for argv in sys.argv:
		if argv[: 12] == "--file_path=":
			file_path = argv[12:]
		if argv[: 9] == "--height=":
			height = int(argv[9:])
		if argv[: 9] == "--weight=":
			weight = int(argv[9:])
		if argv[: 12] == "--time_slot=":
			time_slot = int(argv[12:])

	table = Table(height = height, weight = weight, file_path = file_path)

	
	while 1:
		os.system('clear')
		print(table.show_table())
		table.next_generation()
		time.sleep(time_slot)

