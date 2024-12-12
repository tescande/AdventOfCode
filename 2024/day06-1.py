#!/bin/env python
# Solution 5030

import sys

directions = (
	(-1,  0), # up
	( 0,  1), # right
	( 1,  0), # down
	( 0, -1), # left
)

def print_map(map):
	for line in map:
		print(f"{''.join(line)}")
	print("")

def get_map_cell(map, row, col):
	if row < 0 or col < 0:
		return None

	try:
		return map[row][col]
	except:
		return None

def set_map_cell(map, row, col, val):
	map[row][col] = val

def walk(map, start_row, start_col):
	dir = 0;
	row = start_row
	col = start_col
	res = 1

	set_map_cell(map, row, col, 'X')

	while (True):
		n_row = row + directions[dir][0]
		n_col = col + directions[dir][1]
		cell = get_map_cell(map, n_row, n_col)
		match cell:
			case None:
				# ~ print_map(map)
				# ~ print(n_row, n_col)
				return res
			case '.':
				res += 1
				set_map_cell(map, n_row, n_col, 'X')
				row = n_row
				col = n_col
			case 'X':
				row = n_row
				col = n_col
			case '#':
				dir = (dir + 1) % 4

def main():
	res = 0
	map = []
	start_row = 0
	start_col = 0
	file = sys.argv[1] if len(sys.argv)>=2 else 'day06-input.txt'
	with open(file, 'r') as f:
		for r, line in enumerate(f):
			if '^' in line:
				start_row = r
				start_col = line.index('^')
			map.append(list(line[:-1]))

	print(f"res: {walk(map, start_row, start_col)}")

if __name__ == "__main__":
    exit(main())
