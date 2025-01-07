#!/bin/env python
# Solution 1928

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

def is_loop(map, start_row, start_col):
	dir = 0;
	row = start_row
	col = start_col

	seen = set()
	seen.add((row, col, dir))
	while (True):
		n_row = row + directions[dir][0]
		n_col = col + directions[dir][1]

		if (n_row, n_col, dir) in seen:
			return True

		seen.add((n_row, n_col, dir))

		cell = get_map_cell(map, n_row, n_col)
		match cell:
			case None:
				return False
			case '.' | '^':
				row = n_row
				col = n_col
			case '#':
				dir = (dir + 1) % 4
	return False

def main():
	res = 0
	map = []
	start_row = 0
	start_col = 0
	file = sys.argv[1] if len(sys.argv)>=2 else 'day06-input.txt'
	with open(file, 'r') as f:
		for r, line in enumerate(f):
			if '^' in line:
				start_col = line.index('^')
				start_row = r
			map.append(list(line[:-1]))

	for r, row in enumerate(map):
		for c, val in enumerate(row):
			if val != '.':
				continue

			map[r][c] = '#'
			if is_loop(map, start_row, start_col):
				res += 1
			map[r][c] = '.'

	print(f"res: {res}")

if __name__ == "__main__":
    exit(main())
